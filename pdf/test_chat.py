
# from app.chat import build_chat, ChatArgs
from app.chat import create_embeddings_for_pdf

conversation_id = "123"
pdf_id = "123456"

# chat_args = ChatArgs(
#     conversation_id=conversation_id,
#     pdf_id=pdf_id,
#     # streaming=streaming,
#     metadata={
#         "conversation_id": conversation_id,
#         # "user_id": g.user.id,
#         "pdf_id": pdf_id,
#     },
# )
#
# chat = build_chat(chat_args)
#
# print(chat)
