import json
import urllib3

class Methods:
    def __init__(self, token):
        self.token = token
        self.api_url = f"https://api.telegram.org/bot{self.token}"
        self.http = urllib3.PoolManager()

    def _make_request(self, method, params=None, files=None):
        url = f"{self.api_url}/{method}"
        response = self.http.request(
            'POST',
            url,
            body=json.dumps(params) if params else None,
            headers={'Content-Type': 'application/json'},
            fields=files
        )
        return json.loads(response.data.decode('utf-8'))

    def get_me(self, **kwargs):
        return self._make_request('getMe', params=kwargs)

    def log_out(self, **kwargs):
        return self._make_request('logOut', params=kwargs)

    def close(self, **kwargs):
        """
        Closes the bot instance.
    
        Parameters:
            kwargs: Additional optional parameters.
    
        Returns:
            Response: The response from the Telegram API.
        """
        return self._make_request('close', params=kwargs)

    def get_file(self, file_id, **kwargs):
        """
        Retrieves file information.
    
        Parameters:
            file_id (str): The ID of the file.
            kwargs: timeout (int).
    
        Returns:
            Response: The response from the Telegram API.
        """
        return self._make_request('getFile', params={'file_id': file_id, **kwargs})

    def send_message(self, chat_id, text, **kwargs):
        """
        Sends a message to a chat.
    
        Parameters:
            chat_id (str): The ID of the target chat.
            text (str): The text of the message.
            kwargs: 
                reply_markup (dict): Inline or reply keyboard options.
                parse_mode (str): Text formatting mode.
                disable_notification (bool): Disable notifications.
                timeout (int): Request timeout.
                entities (list): Special entities in the message.
                protect_content (bool): Prevent forwarding the message.
                message_thread_id (int): Unique thread ID.
                reply_parameters (dict): Reply to specific message parameters.
                link_preview_options (dict): Options for link preview.
                business_connection_id (str): Business connection identifier.
                message_effect_id (str): Special message effects.
    
        Returns:
            Response: The response from the Telegram API.
        """
        payload = {'chat_id': str(chat_id), 'text': text}
        payload.update(kwargs)
        return self._make_request('sendMessage', params=payload)

    def delete_message(self, chat_id, message_id, **kwargs):
        """
        Deletes a message in a specified chat.
        
        Parameters:
            chat_id (str): The ID of the chat where the message is located.
            message_id (int): The ID of the message to delete.
            kwargs: Additional parameters such as:
                    timeout (int), protect_content (bool), business_connection_id (str), 
                    message_effect_id (str).
        
        Returns:
            Response: The response from the Telegram API.
        """
        
        payload = {
            'chat_id': chat_id,
            'message_id': message_id
        }
        payload.update(kwargs)
        return self._make_request('deleteMessage', params=payload)

    def set_webhook(self, url=None, certificate=None, **kwargs):
        """
        Sets the webhook for receiving updates.
    
        Parameters:
            url (str): The webhook URL.
            certificate (file): A public key certificate.
            kwargs: 
                max_connections (int): Maximum allowed connections.
                allowed_updates (list): List of allowed update types.
                ip_address (str): Fixed IP address.
                drop_pending_updates (bool): Drop pending updates.
                timeout (int): Request timeout.
                secret_token (str): Secret token for verification.
    
        Returns:
            Response: The response from the Telegram API.
        """
        payload = {'url': url if url else ""}
        files = {'certificate': certificate} if certificate else None
        payload.update(kwargs)
        return self._make_request('setWebhook', params=payload, files=files)

    def delete_webhook(self, **kwargs):
        """
        Deletes the webhook and switches back to getUpdates.
    
        Parameters:
            kwargs: 
                drop_pending_updates (bool): Drop pending updates.
                timeout (int): Request timeout.
    
        Returns:
            Response: The response from the Telegram API.
        """
        return self._make_request('deleteWebhook', params=kwargs)

    def get_webhook_info(self, **kwargs):
        """
        Retrieves information about the webhook.
    
        Parameters:
            kwargs: timeout (int).
    
        Returns:
            Response: The response from the Telegram API.
        """
        return self._make_request('getWebhookInfo', params=kwargs)

    def get_updates(self, **kwargs):
        """
        Retrieves updates using long polling.
    
        Parameters:
            kwargs: 
                offset (int): Identifier of the first update to be returned.
                limit (int): Maximum number of updates to return.
                timeout (int): Timeout for long polling.
                allowed_updates (list): List of allowed update types.
                long_polling_timeout (int): Timeout for long polling.
    
        Returns:
            Response: The response from the Telegram API.
        """
        return self._make_request('getUpdates', params=kwargs)

    def get_user_profile_photos(self, user_id, **kwargs):
        """
        Retrieves a list of profile pictures for a user.
    
        Parameters:
            user_id (str): The ID of the target user.
            kwargs: 
                offset (int): Sequential number of the first photo to be returned.
                limit (int): Limits the number of photos returned.
    
        Returns:
            Response: The response from the Telegram API.
        """
        payload = {'user_id': user_id}
        payload.update(kwargs)
        return self._make_request('getUserProfilePhotos', params=payload)

    def set_message_reaction(self, chat_id, message_id, **kwargs):
        """
        Sets a reaction to a message.
    
        Parameters:
            chat_id (str): The ID of the chat.
            message_id (int): The ID of the message.
            kwargs: 
                reaction (list): List of reactions.
                is_big (bool): Whether the reaction should be big.
    
        Returns:
            Response: The response from the Telegram API.
        """
        payload = {'chat_id': chat_id, 'message_id': message_id}
        payload.update(kwargs)
        return self._make_request('setMessageReaction', params=payload)

    def get_chat(self, chat_id, **kwargs):
        """
        Retrieves information about a chat.
    
        Parameters:
            chat_id (str): The ID of the chat.
            kwargs: Additional optional parameters.
    
        Returns:
            Response: The response from the Telegram API.
        """
        payload = {'chat_id': chat_id}
        payload.update(kwargs)
        return self._make_request('getChat', params=payload)

    def leave_chat(self, chat_id, **kwargs):
        """
        Leaves a chat.
    
        Parameters:
            chat_id (str): The ID of the chat.
            kwargs: Additional optional parameters.
    
        Returns:
            Response: The response from the Telegram API.
        """
        payload = {'chat_id': chat_id}
        payload.update(kwargs)
        return self._make_request('leaveChat', params=payload)

    def get_chat_administrators(self, chat_id, **kwargs):
        """
        Retrieves a list of chat administrators.
    
        Parameters:
            chat_id (str): The ID of the chat.
            kwargs: Additional optional parameters.
    
        Returns:
            Response: The response from the Telegram API.
        """
        payload = {'chat_id': chat_id}
        payload.update(kwargs)
        return self._make_request('getChatAdministrators', params=payload)

    def get_chat_member_count(self, chat_id, **kwargs):
        """
        Retrieves the number of members in a chat.
    
        Parameters:
            chat_id (str): The ID of the chat.
            kwargs: Additional optional parameters.
    
        Returns:
            Response: The response from the Telegram API.
        """
        payload = {'chat_id': chat_id}
        payload.update(kwargs)
        return self._make_request('getChatMemberCount', params=payload)

    def set_sticker_set_thumbnail(self, name, user_id, thumbnail, format):
        """
        Sets the thumbnail for a sticker set.
    
        Parameters:
            name (str): The name of the sticker set.
            user_id (int): The user ID of the sticker set owner.
            thumbnail (file/str): Thumbnail image file or string ID.
            format (str): The format of the thumbnail.
    
        Returns:
            Response: The response from the Telegram API.
        """
        payload = {'name': name, 'user_id': user_id, 'format': format}
        files = {}
        if thumbnail:
            if not isinstance(thumbnail, str):
                files['thumbnail'] = thumbnail
            else:
                payload['thumbnail'] = thumbnail
        return self._make_request('setStickerSetThumbnail', params=payload, files=files or None)

    def replace_sticker_in_set(self, user_id, name, old_sticker, sticker):
        """
        Replaces a sticker in a set.
    
        Parameters:
            user_id (int): The user ID of the sticker set owner.
            name (str): The name of the sticker set.
            old_sticker (str): The old sticker ID.
            sticker (object): The new sticker object.
    
        Returns:
            Response: The response from the Telegram API.
        """
        payload = {'user_id': user_id, 'name': name, 'old_sticker': old_sticker, 'sticker': sticker.to_json()}
        return self._make_request('replaceStickerInSet', params=payload)

    def set_chat_sticker_set(self, chat_id, sticker_set_name):
        """
        Sets the sticker set for a chat.
    
        Parameters:
            chat_id (str): The ID of the chat.
            sticker_set_name (str): The name of the sticker set.
    
        Returns:
            Response: The response from the Telegram API.
        """
        payload = {'chat_id': chat_id, 'sticker_set_name': sticker_set_name}
        return self._make_request('setChatStickerSet', params=payload)

    def delete_chat_sticker_set(self, chat_id):
        """
        Deletes the sticker set from a chat.
    
        Parameters:
            chat_id (str): The ID of the chat.
    
        Returns:
            Response: The response from the Telegram API.
        """
        payload = {'chat_id': chat_id}
        return self._make_request('deleteChatStickerSet', params=payload)

    def get_chat_member(self, chat_id, user_id):
        """
        Retrieves information about a member
        """
        payload = {'chat_id': chat_id, 'user_id': user_id}
        return self._make_request('getChatMember', params=payload)

    def forward_message(self, chat_id, from_chat_id, message_id, **kwargs):
        """
        Forwards a message from one chat to another.
    
        Parameters:
            chat_id (str): The ID of the target chat.
            from_chat_id (str): The ID of the chat from which to forward the message.
            message_id (int): The ID of the message to forward.
            kwargs: disable_notification (bool), timeout (int), protect_content (bool), 
                    message_thread_id (int).
    
        Returns:
            Response: The response from the Telegram API.
        """
        
        payload = {'chat_id': chat_id, 'from_chat_id': from_chat_id, 'message_id': message_id}
        payload.update(kwargs)
        return self._make_request('forwardMessage', params=payload)

    def copy_message(self, chat_id, from_chat_id, message_id, **kwargs):
        """
        Copies a message from one chat to another.
    
        Parameters:
            chat_id (str): The ID of the target chat.
            from_chat_id (str): The ID of the chat from which to copy the message.
            message_id (int): The ID of the message to copy.
            kwargs: caption (str), parse_mode (str), caption_entities (list), disable_notification (bool),
                    reply_markup (dict), timeout (int), protect_content (bool), message_thread_id (int),
                    reply_parameters (dict), show_caption_above_media (bool).
    
        Returns:
            Response: The response from the Telegram API.
        """
        
        payload = {'chat_id': chat_id, 'from_chat_id': from_chat_id, 'message_id': message_id}
        payload.update(kwargs)
        return self._make_request('copyMessage', params=payload)

    def send_dice(self, chat_id, **kwargs):
        """
        Sends a dice emoji to a specified chat.
    
        Parameters:
            chat_id (str): The ID of the target chat.
            kwargs: emoji (str), disable_notification (bool), reply_markup (dict), timeout (int), 
                    protect_content (bool), message_thread_id (int), reply_parameters (dict),
                    business_connection_id (str), message_effect_id (str).
    
        Returns:
            Response: The response from the Telegram API.
        """
        
        payload = {'chat_id': chat_id}
        payload.update(kwargs)
        return self._make_request('sendDice', params=payload)

    def send_photo(self, chat_id, photo, **kwargs):
        """
        Sends a photo to a specified chat.
    
        Parameters:
            chat_id (str): The ID of the chat.
            photo (str or file): The photo to send.
            kwargs: caption (str), reply_markup (dict), parse_mode (str), disable_notification (bool), 
                    timeout (int), caption_entities (list), protect_content (bool), message_thread_id (int),
                    has_spoiler (bool), reply_parameters (dict), business_connection_id (str), 
                    message_effect_id (str), show_caption_above_media (bool).
    
        Returns:
            Response: The response from the Telegram API.
        """
    
        payload = {'chat_id': chat_id}
        files = None
        
        if isinstance(photo, str):
            payload['photo'] = photo
        else:
            files = {'photo': photo}
    
        payload.update(kwargs)
        return self._make_request('sendPhoto', params=payload, files=files)

    def send_photo(chat_id, photo, **kwargs):
        """
        Sends a photo to a specified chat.
        
        Parameters:
            chat_id (str): The ID of the chat.
            photo (str or file): The photo to send.
            kwargs: Other optional parameters for sending the photo.
        
        Returns:
            Response: The response from the Telegram API.
        """
        
        payload = {'chat_id': chat_id}
        files = None
    
        if isinstance(photo, str):
            payload['photo'] = photo
        else:
            files = {'photo': photo}
    
        payload.update(kwargs)
        return self._make_request('sendPhoto', params=payload, files=files)

    def send_media_group(self, chat_id, media, **kwargs):
        """
        Sends a group of photos or videos as an album.
    
        Parameters:
            chat_id (str): The ID of the target chat.
            media (list): A list of media files to send.
            kwargs: disable_notification (bool), timeout (int), protect_content (bool), 
                    message_thread_id (int), reply_parameters (dict), business_connection_id (str),
                    message_effect_id (str).
    
        Returns:
            Response: The response from the Telegram API.
        """
        
        media_json = [{'type': item['type'], 'media': item['media']} for item in media]
        payload = {'chat_id': chat_id, 'media': media_json}
        payload.update(kwargs)
        files = [item['media'] for item in media if isinstance(item['media'], (str, bytes))]
        return self._make_request('sendMediaGroup', params=payload, files=files or None, method='post' if files else 'get')

    def send_location(self, chat_id, latitude, longitude, **kwargs):
        """
        Sends a location to a specified chat.
    
        Parameters:
            chat_id (str): The ID of the target chat.
            latitude (float): The latitude of the location.
            longitude (float): The longitude of the location.
            kwargs: live_period (int), reply_markup (dict), disable_notification (bool), timeout (int),
                    horizontal_accuracy (float), heading (float), proximity_alert_radius (float),
                    protect_content (bool), message_thread_id (int), reply_parameters (dict),
                    business_connection_id (str), message_effect_id (str).
    
        Returns:
            Response: The response from the Telegram API.
        """
        
        payload = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude
        }
        payload.update(kwargs)
        return self._make_request('sendLocation', params=payload)

    def edit_message_live_location(self, latitude, longitude, **kwargs):
        """
        Edits the live location of a message.
    
        Parameters:
            latitude (float): The updated latitude.
            longitude (float): The updated longitude.
            kwargs: chat_id (str), message_id (int), inline_message_id (str), reply_markup (dict), 
                    timeout (int), horizontal_accuracy (float), heading (float), proximity_alert_radius (float),
                    live_period (int), business_connection_id (str).
    
        Returns:
            Response: The response from the Telegram API.
        """
        
        payload = {
            'latitude': latitude,
            'longitude': longitude
        }
        payload.update(kwargs)
        return self._make_request('editMessageLiveLocation', params=payload)

    def stop_message_live_location(self, **kwargs):
        """
        Stops sharing the live location of a message.
    
        Parameters:
            kwargs: chat_id (str), message_id (int), inline_message_id (str), reply_markup (dict), 
                    timeout (int), business_connection_id (str).
    
        Returns:
            Response: The response from the Telegram API.
        """
        
        payload = {}
        payload.update(kwargs)
        return self._make_request('stopMessageLiveLocation', params=payload)

    def send_venue(self, chat_id, latitude, longitude, title, address, **kwargs):
        """
        Sends a venue (location with additional details) to a specified chat.
    
        Parameters:
            chat_id (str): The ID of the chat.
            latitude (float): The latitude of the venue.
            longitude (float): The longitude of the venue.
            title (str): The title of the venue.
            address (str): The address of the venue.
            kwargs: foursquare_id (str), foursquare_type (str), disable_notification (bool), reply_markup (dict),
                    timeout (int), google_place_id (str), google_place_type (str), protect_content (bool),
                    message_thread_id (int), reply_parameters (dict), business_connection_id (str),
                    message_effect_id (str).
    
        Returns:
            Response: The response from the Telegram API.
        """
        
        payload = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude,
            'title': title,
            'address': address
        }
        payload.update(kwargs)
        return self._make_request('sendVenue', params=payload)

    def send_contact(self, chat_id, phone_number, first_name, **kwargs):
        """
        Sends a contact to a specified chat.
    
        Parameters:
            chat_id (str): The ID of the chat where the contact will be sent.
            phone_number (str): The contact's phone number.
            first_name (str): The contact's first name.
            last_name (str, optional): The contact's last name.
            vcard (str, optional): Additional vCard information.
            kwargs: disable_notification (bool), reply_markup (dict), timeout (int),
                    protect_content (bool), message_thread_id (int), reply_parameters (dict),
                    business_connection_id (str), message_effect_id (str).
    
        Returns:
            Response: The response from the Telegram API.
        """
        
        payload = {
            'chat_id': chat_id,
            'phone_number': phone_number,
            'first_name': first_name
        }
        payload.update(kwargs)
        return self._make_request('sendContact', params=payload)

    def send_chat_action(self, chat_id, action, **kwargs):
        """
        Sends a chat action to a specified chat (e.g., 'typing', 'upload_photo').
    
        Parameters:
            chat_id (str): The ID of the chat.
            action (str): The action to broadcast.
            kwargs: timeout (int), message_thread_id (int), business_connection_id (str).
    
        Returns:
            Response: The response from the Telegram API.
        """
        
        payload = {
            'chat_id': chat_id,
            'action': action
        }
        payload.update(kwargs)
        return self._make_request('sendChatAction', params=payload)

    def send_video(self, chat_id, video, **kwargs):
        """
        Sends a video file to a specified chat.
    
        Parameters:
            chat_id (str): The ID of the chat.
            video (str or file): The video file to send.
            kwargs: duration (int), caption (str), reply_markup (dict), parse_mode (str), supports_streaming (bool),
                    disable_notification (bool), timeout (int), thumbnail (str or file), width (int), height (int),
                    caption_entities (list), protect_content (bool), message_thread_id (int), has_spoiler (bool),
                    reply_parameters (dict), business_connection_id (str), message_effect_id (str),
                    show_caption_above_media (bool).
    
        Returns:
            Response: The response from the Telegram API.
        """
        
        payload = {'chat_id': chat_id}
        files = {}
        if isinstance(video, str):
            payload['video'] = video
        else:
            files['video'] = video
        payload.update(kwargs)
        return self._make_request('sendVideo', params=payload, files=files)

    def send_animation(self, chat_id, animation, **kwargs):
        """
        Sends an animation (GIF) to a specified chat.
    
        Parameters:
            chat_id (str): The ID of the chat.
            animation (str or file): The animation to send.
            kwargs: duration (int), caption (str), reply_markup (dict), parse_mode (str),
                    disable_notification (bool), timeout (int), thumbnail (str or file),
                    caption_entities (list), protect_content (bool), width (int), height (int),
                    message_thread_id (int), reply_parameters (dict), has_spoiler (bool),
                    business_connection_id (str), message_effect_id (str), show_caption_above_media (bool).
    
        Returns:
            Response: The response from the Telegram API.
        """
        
        payload = {'chat_id': chat_id}
        files = {}
        if isinstance(animation, str):
            payload['animation'] = animation
        else:
            files['animation'] = animation
        payload.update(kwargs)
        return self._make_request('sendAnimation', params=payload, files=files)

    def send_voice(self, chat_id, voice, **kwargs):
        """
        Sends a voice message to a specified chat.
    
        Parameters:
            chat_id (str): The ID of the chat.
            voice (str or file): The voice file to send.
            kwargs: caption (str), duration (int), reply_markup (dict), parse_mode (str),
                    disable_notification (bool), timeout (int), caption_entities (list),
                    protect_content (bool), message_thread_id (int), reply_parameters (dict),
                    business_connection_id (str), message_effect_id (str).
    
        Returns:
            Response: The response from the Telegram API.
        """
        
        payload = {'chat_id': chat_id}
        files = {}
        if isinstance(voice, str):
            payload['voice'] = voice
        else:
            files['voice'] = voice
        payload.update(kwargs)
        return self._make_request('sendVoice', params=payload, files=files)

    def send_video_note(self, chat_id, video_note, **kwargs):
        """
        Sends a video note to a specified chat.
    
        Parameters:
            chat_id (str): The ID of the chat.
            video_note (str or file): The video note to send.
            kwargs: duration (int), length (int), reply_markup (dict), disable_notification (bool),
                    timeout (int), thumbnail (str or file), protect_content (bool),
                    message_thread_id (int), reply_parameters (dict), business_connection_id (str),
                    message_effect_id (str).
    
        Returns:
            Response: The response from the Telegram API.
        """
        
        payload = {'chat_id': chat_id}
        files = {}
        if isinstance(video_note, str):
            payload['video_note'] = video_note
        else:
            files['video_note'] = video_note
        payload.update(kwargs)
        return self._make_request('sendVideoNote', params=payload, files=files)

    def send_audio(self, chat_id, audio, **kwargs):
        print(kwargs)
        """
        Sends an audio file to a specified chat.
    
        Parameters:
            chat_id (str): The ID of the chat where the audio will be sent.
            audio (str or file): The audio file to send (can be a file path or URL).
            caption (str, optional): Caption for the audio message.
            reply_markup (dict, optional): Additional reply markup.
            parse_mode (str, optional): Parse mode for the caption.
            duration (int, optional): Duration of the audio in seconds.
            performer (str, optional): Performer of the audio.
            title (str, optional): Title of the audio.
            thumb (str or file, optional): Thumbnail for the audio (can be a file path or URL).
            disable_notification (bool, optional): Sends the message silently.
            timeout (int, optional): Request timeout.
            reply_parameters (dict, optional): Additional parameters for replies.
            has_spoiler (bool, optional): Indicates if the audio has spoilers.
            message_thread_id (int, optional): The message thread ID for the reply.
            business_connection_id (str, optional): Business connection ID for the message.
            message_effect_id (str, optional): Message effect ID for the audio.
    
        Returns:
            Response: The response from the Telegram API.
        """
        
        payload = {'chat_id': chat_id}
        files = {}
        if isinstance(audio, str):
            payload['audio'] = audio
        else:
            files['audio'] = audio

        payload.update(kwargs)
        return self._make_request('sendAudio', params=payload, files=files)
    
    def send_sticker(self, chat_id, sticker, **kwargs):
        """
        Sends a sticker to a specified chat.
    
        Parameters:
            chat_id (str): The ID of the chat where the sticker will be sent.
            sticker (str or file): The sticker to send (can be a file path or URL).
            disable_notification (bool, optional): Sends the message silently.
            reply_markup (dict, optional): Additional reply markup.
            timeout (int, optional): Request timeout.
            reply_parameters (dict, optional): Additional parameters for replies.
            message_thread_id (int, optional): The message thread ID for the reply.
    
        Returns:
            Response: The response from the Telegram API.
        """
    
        payload = {'chat_id': chat_id}
        files = {}
        if isinstance(sticker, str):
            payload['sticker'] = sticker
        else:
            files['sticker'] = sticker
        payload.update(kwargs)
        return self._make_request('sendSticker', params=payload, files=files)
    
    def answer_inline_query(self, inline_query_id, results, **kwargs):
        """
        Sends answers to an inline query.
    
        Parameters:
            inline_query_id (str): Unique identifier for the answered inline query.
            results (list): A list of InlineQueryResult objects to be sent as the response.
                Each result must contain at least the following fields:
                - id (str): Unique identifier for the result.
                - type (str): Type of the result (e.g., 'voice').
                - voice (str): URL of the voice message.
                - title (str): Title of the result.
                - caption (str, optional): Caption for the voice message.
            kwargs: Additional optional parameters that can be included in the request.
                - cache_time (int, optional): The time in seconds that the results of the query
                  may be cached on the client side. Default is 0.
                - is_personal (bool, optional): Pass True if results may be cached for a
                  specific user. Defaults to False.
                - next_offset (str, optional): Offset for the next inline query results.
                - switch_pm_text (str, optional): Text of the button for switching to a private chat with the bot.
                - switch_pm_parameter (str, optional): Deep-linking parameter for the bot.
        
        Returns:
            Response: The response from the Telegram API.
        """
        
        params = {
            'inline_query_id': inline_query_id,
            'results': json.dumps(results),
            **kwargs
        }
        return self._make_request('answerInlineQuery', params=params)