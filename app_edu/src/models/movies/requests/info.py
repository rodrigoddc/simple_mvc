from typing import Dict
from src.models.movies.requests.tmdb_api_caller import tmdb_api_caller, tmdb_response_handler
import asyncio, aiohttp
from abc import ABC, abstractmethod

class InfoRequestStrategy(ABC):
    def __init__(self, movie_id: int) -> None:
        self.movie_id = movie_id
        self.urls = [
            self._movie_details_url(), 
            self._movie_crew_url()
        ]

    def _movie_details_url(self):
        return f"movie/{self.movie_id}"

    def _movie_crew_url(self):
        return f"movie/{self.movie_id}/credits"
    
    @abstractmethod
    def perform_request(self) -> Dict:
        pass


class AsyncInfoRequest(InfoRequestStrategy):

    async def fetch_movie_details_and_movie_crew(self):
        async with aiohttp.ClientSession() as session:
            results = []
            tasks = self.get_tasks(self.urls, session)
            responses = await asyncio.gather(*tasks)
            for response in responses:
                results.append(await tmdb_response_handler(response))
            
            return results

    def get_tasks(self, urls, session):
        tasks = []
        for url in urls:
            tasks.append(asyncio.create_task(
                tmdb_api_caller(
                    url=url, 
                    method="GET", 
                    session=session
                    )
                )
            )
        return tasks

    def perform_request(self):
        movie_data, crew_data = asyncio.run(
        self.fetch_movie_details_and_movie_crew()
        )
        return movie_data | crew_data


class SyncInfoRequest(InfoRequestStrategy):
    def perform_request(self):
        responses = []
        for url in self.urls:
            responses.append(tmdb_api_caller(
                        url=url, 
                        method="GET",
                        )
            )
        movie_data, crew_data = responses[0].json(), responses[1].json()
        return movie_data | crew_data

class InfoRequest():
    def __init__(self, movie_id: int, strategy: InfoRequestStrategy) -> None:
        self.movie_id = movie_id
        self.strategy = strategy

    def get_movie_info(self):
        if self.strategy == "async":
            return AsyncInfoRequest(self.movie_id).perform_request()
        
        return SyncInfoRequest(self.movie_id).perform_request()
