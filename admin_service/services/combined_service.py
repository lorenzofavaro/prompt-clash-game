from models.round import Round
from services.chat_service import chat_service
from services.rounds_service import rounds_service


class CombinedService:
    def __init__(self):
        self._rounds_service = rounds_service
        self._chat_service = chat_service

    async def latest_image_per_user(self):
        response, status_code = await self._rounds_service.last()

        if response.get('round', None):
            last_round = Round.model_validate(response['round'])

            return await self._chat_service.latest_round_image_per_user(
                last_round.start_timestamp, last_round.end_timestamp
            )
        return response, status_code


combined_service = CombinedService()
