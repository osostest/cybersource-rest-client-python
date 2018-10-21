# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class KeyGenerationApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def generate_public_key(self, generate_public_key_request, **kwargs):
        """
        Generate Key
        Generate a one-time use public key and key ID to encrypt the card number in the follow-on Tokenize Card request. The key used to encrypt the card number on the cardholder’s device or browser is valid for 15 minutes and must be used to verify the signature in the response message. CyberSource recommends creating a new key for each order. Generating a key is an authenticated request initiated from your servers, prior to requesting to tokenize the card data from your customer’s device or browser.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.generate_public_key(generate_public_key_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param GeneratePublicKeyRequest generate_public_key_request: (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.generate_public_key_with_http_info(generate_public_key_request, **kwargs)
        else:
            (data) = self.generate_public_key_with_http_info(generate_public_key_request, **kwargs)
            return data

    def generate_public_key_with_http_info(self, generate_public_key_request, **kwargs):
        """
        Generate Key
        Generate a one-time use public key and key ID to encrypt the card number in the follow-on Tokenize Card request. The key used to encrypt the card number on the cardholder’s device or browser is valid for 15 minutes and must be used to verify the signature in the response message. CyberSource recommends creating a new key for each order. Generating a key is an authenticated request initiated from your servers, prior to requesting to tokenize the card data from your customer’s device or browser.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.generate_public_key_with_http_info(generate_public_key_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param GeneratePublicKeyRequest generate_public_key_request: (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['generate_public_key_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_public_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'generate_public_key_request' is set
        if ('generate_public_key_request' not in params) or (params['generate_public_key_request'] is None):
            raise ValueError("Missing the required parameter `generate_public_key_request` when calling `generate_public_key`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'generate_public_key_request' in params:
            body_params = params['generate_public_key_request']
            # HTTP header `Accept`
            header_params['Accept'] = self.api_client. \
                select_header_accept(['application/json'])
            header_params['Content-Type'] = self.api_client. \
                select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/flex/v1/keys/', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse200',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
