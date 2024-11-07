import time
import json

from flask import Flask, request
from .methods import Methods
from .utils import to_namedtuple

class Bot(Methods):
    def __init__(self, token, name=None, webhook=None):
        super().__init__(token)
        self.handlers = {
            "message": [],
            "edited_message": [],
            "channel_post": [],
            "edited_channel_post": [],
            "inline_query": [],
            "chosen_inline_result": [],
            "callback_query": [],
            "shipping_query": [],
            "pre_checkout_query": [],
            "poll": [],
            "poll_answer": [],
            "my_chat_member": [],
            "chat_member": [],
            "chat_join_request": [],
            "message_reaction": [],
            "message_reaction_count": [],
            "chat_boost": [],
            "removed_chat_boost": [],
            "business_connection": [],
            "business_message": [],
            "edited_business_message": [],
            "deleted_business_messages": [],
        }
        self.webhook = webhook
        self.name = name
        self.app = Flask(__name__)
        self.process_webhook = self.app
        self.me = self.get_me()

        @self.app.route(f'/{name}/webhook', methods=['POST'])
        def handle_update():
            update = request.get_json()
            print(update)
            update_type = self.extract_main_key(update)
            self.process_new_updates(update_type, update[update_type])

            return 'OK', 200

    def extract_main_key(self, data):
        for key in data.keys():
                if isinstance(data[key], dict):  # التأكد أن القيمة هي قاموس
                    return key  # إرجاع المفتاح الرئيسي
        return None

    def message_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["message"].append((filter_func, func))
            return func
        return decorator

    def edited_message_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["edited_message"].append((filter_func, func))
            return func
        return decorator

    def channel_post_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["channel_post"].append((filter_func, func))
            return func
        return decorator

    def edited_channel_post_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["edited_channel_post"].append((filter_func, func))
            return func
        return decorator

    def inline_query_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["inline_query"].append((filter_func, func))
            return func
        return decorator

    def chosen_inline_result_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["chosen_inline_result"].append((filter_func, func))
            return func
        return decorator

    def callback_query_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["callback_query"].append((filter_func, func))
            return func
        return decorator

    def shipping_query_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["shipping_query"].append((filter_func, func))
            return func
        return decorator

    def pre_checkout_query_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["pre_checkout_query"].append((filter_func, func))
            return func
        return decorator

    def poll_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["poll"].append((filter_func, func))
            return func
        return decorator

    def poll_answer_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["poll_answer"].append((filter_func, func))
            return func
        return decorator

    def my_chat_member_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["my_chat_member"].append((filter_func, func))
            return func
        return decorator

    def chat_member_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["chat_member"].append((filter_func, func))
            return func
        return decorator

    def chat_join_request_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["chat_join_request"].append((filter_func, func))
            return func
        return decorator

    def message_reaction_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["message_reaction"].append((filter_func, func))
            return func
        return decorator

    def message_reaction_count_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["message_reaction_count"].append((filter_func, func))
            return func
        return decorator

    def chat_boost_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["chat_boost"].append((filter_func, func))
            return func
        return decorator

    def removed_chat_boost_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["removed_chat_boost"].append((filter_func, func))
            return func
        return decorator

    def business_connection_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["business_connection"].append((filter_func, func))
            return func
        return decorator

    def business_message_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["business_message"].append((filter_func, func))
            return func
        return decorator

    def edited_business_message_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["edited_business_message"].append((filter_func, func))
            return func
        return decorator

    def deleted_business_messages_handler(self, filter_func=None):
        def decorator(func):
            self.handlers["deleted_business_messages"].append((filter_func, func))
            return func
        return decorator
    
    def process_new_updates(self, update_type, data):
        data = to_namedtuple(update_type, data)
        #print(f"Processing {update_type}: {data}")
        if update_type in self.handlers:
            for filter_func, handler in self.handlers[update_type]:
                # تحقق مما إذا كان هناك دالة فلتر وتطبيقها
                if filter_func and not filter_func(data):
                    continue
                # استدعاء المعالج مباشرة دون تحقق من وجود خاصية message
                handler(data)  # تمرير البيانات مباشرة إلى المعالج
                return

    def process_new_updates(self, update_type, data):
        data = to_namedtuple(update_type, data)
        #print(f"Processing {update_type}: {data}")
    
        if update_type in self.handlers:
            for filter_func, handler in self.handlers[update_type]:
                try:
                    if filter_func and not filter_func(data):
                        continue
                except Exception as e:
                    # print(f"\033[91mError in filter function: {e}\033[0m")  # 91 هو كود اللون الأحمر
                    continue
    
                handler(data)
                return

    def get_me(self):
        response = self._make_request('getMe')
        if response["ok"]:
            return to_namedtuple("BotInfo", response['result'])
        else:
            raise Exception("INVALID BOT TOKEN")

    def run(self):
        if self.webhook:
            print(f"Running with Webhook")
            self.app.run(host='0.0.0.0', port=5000)
        else:
            print("Running with polling (infinity mode)")
            self.infinity_polling()

    def infinity_polling(self):
        offset = 0
        while True:
            try:
                updates = self._make_request('getUpdates', params={'offset': offset, 'timeout': 100})
                print("\033[32m", "Updates received:", json.dumps(updates, indent=4, ensure_ascii=False), "\033[0m", "\n")
                if updates['ok']:
                    for update in updates['result']:
                        update_type = self.extract_main_key(update)
                        self.process_new_updates(update_type, update[update_type])
                        offset = max(offset, update['update_id'] + 1)
            except Exception as e:
                print(f"An error occurred: {e}")  # إدارة الاستثناءات
            time.sleep(1)
