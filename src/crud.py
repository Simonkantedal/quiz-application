from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId

from src.models import Question, Team


class CRUD:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db

    async def create_question(self, question: Question):
        result = await self.db.questions.insert_one(question.dict())
        return str(result.inserted_id)

    async def get_question(self, question_id: str):
        question = await self.db.questions.find_one({"_id": ObjectId(question_id)})
        return question

    async def update_question(self, question_id: str, question: Question):
        await self.db.questions.update_one(
            {"_id": ObjectId(question_id)}, {"$set": question.dict()}
        )
        return await self.get_question(question_id)

    async def delete_question(self, question_id: str):
        result = await self.db.questions.delete_one({"_id": ObjectId(question_id)})
        return result.deleted_count > 0

    async def create_team(self, team: Team):
        result = await self.db.teams.insert_one(team.dict())
        return str(result.inserted_id)

    async def get_team(self, team_id: str):
        team = await self.db.teams.find_one({"_id": ObjectId(team_id)})
        return team

    async def update_team(self, team_id: str, team: Team):
        await self.db.teams.update_one(
            {"_id": ObjectId(team_id)}, {"$set": team.dict()}
        )
        return await self.get_team(team_id)

    async def delete_team(self, team_id: str):
        result = await self.db.teams.delete_one({"_id": ObjectId(team_id)})
        return result.deleted_count > 0
