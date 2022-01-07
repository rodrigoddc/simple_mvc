from src.models.movies.requests.tmdb_api_caller import tmdb_api_caller, tmdb_response_handler
import asyncio, aiohttp

class InfoRequest():

    def __init__(self, movie_id: int) -> None:
        self.movie_id: str = movie_id

    async def fetch_movie_details_and_movie_crew(self):
        urls = [
            self._movie_details_url(), 
            self._movie_crew_url()
        ]
        async with aiohttp.ClientSession() as session:
            results = []
            tasks = self.get_tasks(urls, session)
            responses = await asyncio.gather(*tasks)
            for response in responses:
                results.append(await tmdb_response_handler(response))
            
            return results
    
    def _movie_details_url(self):
        return f"movie/{self.movie_id}"

    def _movie_crew_url(self):
        return f"movie/{self.movie_id}/credits"

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
