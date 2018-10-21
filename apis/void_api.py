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


class VoidApi(object):
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

    def get_void(self, id, **kwargs):
        """
        Retrieve A Void
        Include the void ID in the GET request to retrieve the void details.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_void(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The void ID returned from a previous void request. (required)
        :return: InlineResponse2015
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_void_with_http_info(id, **kwargs)
        else:
            (data) = self.get_void_with_http_info(id, **kwargs)
            return data

    def get_void_with_http_info(self, id, **kwargs):
        """
        Retrieve A Void
        Include the void ID in the GET request to retrieve the void details.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_void_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The void ID returned from a previous void request. (required)
        :return: InlineResponse2015
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_void" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_void`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client. \
            select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client. \
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/pts/v2/voids/'+id, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse2015',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def void_capture(self, void_capture_request, id, **kwargs):
        """
        Void a Capture
        Include the capture ID in the POST request to cancel the capture.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.void_capture(void_capture_request, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param VoidCaptureRequest void_capture_request: (required)
        :param str id: The capture ID returned from a previous capture request. (required)
        :return: InlineResponse2015
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.void_capture_with_http_info(void_capture_request, id, **kwargs)
        else:
            (data) = self.void_capture_with_http_info(void_capture_request, id, **kwargs)
            return data

    def void_capture_with_http_info(self, void_capture_request, id, **kwargs):
        """
        Void a Capture
        Include the capture ID in the POST request to cancel the capture.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.void_capture_with_http_info(void_capture_request, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param VoidCaptureRequest void_capture_request: (required)
        :param str id: The capture ID returned from a previous capture request. (required)
        :return: InlineResponse2015
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['void_capture_request', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method void_capture" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'void_capture_request' is set
        if ('void_capture_request' not in params) or (params['void_capture_request'] is None):
            raise ValueError("Missing the required parameter `void_capture_request` when calling `void_capture`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `void_capture`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'void_capture_request' in params:
            body_params = params['void_capture_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client. \
            select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client. \
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/pts/v2/captures/'+id+'/voids', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse2015',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def void_credit(self, void_credit_request, id, **kwargs):
        """
        Void a Credit
        Include the credit ID in the POST request to cancel the credit.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.void_credit(void_credit_request, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param VoidCreditRequest void_credit_request: (required)
        :param str id: The credit ID returned from a previous credit request. (required)
        :return: InlineResponse2015
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.void_credit_with_http_info(void_credit_request, id, **kwargs)
        else:
            (data) = self.void_credit_with_http_info(void_credit_request, id, **kwargs)
            return data

    def void_credit_with_http_info(self, void_credit_request, id, **kwargs):
        """
        Void a Credit
        Include the credit ID in the POST request to cancel the credit.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.void_credit_with_http_info(void_credit_request, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param VoidCreditRequest void_credit_request: (required)
        :param str id: The credit ID returned from a previous credit request. (required)
        :return: InlineResponse2015
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['void_credit_request', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method void_credit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'void_credit_request' is set
        if ('void_credit_request' not in params) or (params['void_credit_request'] is None):
            raise ValueError("Missing the required parameter `void_credit_request` when calling `void_credit`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `void_credit`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'void_credit_request' in params:
            body_params = params['void_credit_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client. \
            select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client. \
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/pts/v2/credits/'+id+'/voids', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse2015',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def void_payment(self, void_payment_request, id, **kwargs):
        """
        Void a Payment
        Include the payment ID in the POST request to cancel the payment.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.void_payment(void_payment_request, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param VoidPaymentRequest void_payment_request: (required)
        :param str id: The payment ID returned from a previous payment request. (required)
        :return: InlineResponse2015
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.void_payment_with_http_info(void_payment_request, id, **kwargs)
        else:
            (data) = self.void_payment_with_http_info(void_payment_request, id, **kwargs)
            return data

    def void_payment_with_http_info(self, void_payment_request, id, **kwargs):
        """
        Void a Payment
        Include the payment ID in the POST request to cancel the payment.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.void_payment_with_http_info(void_payment_request, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param VoidPaymentRequest void_payment_request: (required)
        :param str id: The payment ID returned from a previous payment request. (required)
        :return: InlineResponse2015
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['void_payment_request', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method void_payment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'void_payment_request' is set
        if ('void_payment_request' not in params) or (params['void_payment_request'] is None):
            raise ValueError("Missing the required parameter `void_payment_request` when calling `void_payment`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `void_payment`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'void_payment_request' in params:
            body_params = params['void_payment_request']
        header_params['Accept'] = self.api_client. \
            select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client. \
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/pts/v2/payments/'+id+'/voids', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse2015',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def void_refund(self, void_refund_request, id, **kwargs):
        """
        Void a Refund
        Include the refund ID in the POST request to cancel the refund.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.void_refund(void_refund_request, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param VoidRefundRequest void_refund_request: (required)
        :param str id: The refund ID returned from a previous refund request. (required)
        :return: InlineResponse2015
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.void_refund_with_http_info(void_refund_request, id, **kwargs)
        else:
            (data) = self.void_refund_with_http_info(void_refund_request, id, **kwargs)
            return data

    def void_refund_with_http_info(self, void_refund_request, id, **kwargs):
        """
        Void a Refund
        Include the refund ID in the POST request to cancel the refund.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.void_refund_with_http_info(void_refund_request, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param VoidRefundRequest void_refund_request: (required)
        :param str id: The refund ID returned from a previous refund request. (required)
        :return: InlineResponse2015
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['void_refund_request', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method void_refund" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'void_refund_request' is set
        if ('void_refund_request' not in params) or (params['void_refund_request'] is None):
            raise ValueError("Missing the required parameter `void_refund_request` when calling `void_refund`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `void_refund`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'void_refund_request' in params:
            body_params = params['void_refund_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client. \
            select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client. \
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/pts/v2/refunds/'+id+'/voids', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse2015',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
