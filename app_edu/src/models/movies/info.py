from typing import Dict, Optional
class MovieInfo:
    def __init__(self, json_response: Dict):
        self.movie = json_response
        self.title: str = self._get_title()
        self.year: int = self._get_year()
        self.director: str = self._get_director()
        self.backdrop: Optional[str] = self._get_backdrop()

    def _get_title(self):
        return self.movie["title"]

    def _get_year(self):
        return int(self.movie["release_date"][0:4])

    def _get_director(self):
        crew = self.movie["crew"]

        for worker in crew:
            try:
                if worker["job"] == "Director":
                    return worker["name"]
            except KeyError:
                continue

    def _get_backdrop(self):
        backdrop = self.movie["backdrop_path"]
        if backdrop != "null":
            return backdrop
        else:
            return None
