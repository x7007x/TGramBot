from collections import namedtuple

content_type_media = [
    'text', 'animation', 'audio', 'document', 'photo', 'sticker', 'story', 'video', 'video_note', 'voice', 'contact',
    'dice', 'game', 'poll', 'venue', 'location',  'invoice', 'successful_payment', 'connected_website',
    'passport_data', 'web_app_data',
]

content_type_service = [
    'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo',
    'group_chat_created', 'supergroup_chat_created', 'channel_chat_created', 'message_auto_delete_timer_changed',
    'migrate_to_chat_id', 'migrate_from_chat_id', 'pinned_message', 'users_shared', 'chat_shared',
    'write_access_allowed', 'proximity_alert_triggered', 'forum_topic_created', 'forum_topic_edited',
    'forum_topic_closed', 'forum_topic_reopened', 'general_forum_topic_hidden', 'general_forum_topic_unhidden',
    'giveaway_created', 'giveaway', 'giveaway_winners', 'giveaway_completed', 'video_chat_scheduled',
    'video_chat_started', 'video_chat_ended', 'video_chat_participants_invited',
]

update_types = [
    "message", "edited_message", "channel_post", "edited_channel_post", "inline_query", "chosen_inline_result",
    "callback_query", "shipping_query", "pre_checkout_query", "poll", "poll_answer", "my_chat_member", "chat_member",
    "chat_join_request", "message_reaction", "message_reaction_count", "chat_boost", "removed_chat_boost",
    "business_connection", "business_message", "edited_business_message", "deleted_business_messages"
]

content_type_media = [
    'text', 'animation', 'audio', 'document', 'photo',
    'sticker', 'video', 'voice', 'contact',
]

def to_namedtuple(name, d):
    def sanitize_key(key):
        return key.replace('-', '_').replace(' ', '_').replace('.', '_').replace('from', 'from_user')

    def convert_dict(name, d):
        sanitized_dict = {}
        for key, value in d.items():
            sanitized_key = sanitize_key(key)
            if isinstance(value, dict):
                sanitized_dict[sanitized_key] = convert_dict(sanitized_key, value)
            else:
                sanitized_dict[sanitized_key] = value
        return namedtuple(name, sanitized_dict.keys())(*sanitized_dict.values())
    
    return convert_dict(name, d)

