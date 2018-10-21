from cybersource_rest_client_python.authenticationsdk.util.GlobalLabelParameters import *
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import ast
import json
import cybersource_rest_client_python.authenticationsdk.util.ExceptionAuth
import os
import cybersource_rest_client_python.authenticationsdk.logger.Log


class MerchantConfigaration:

    def __init__(self):
        self.merchant_keyid = None
        self.merchant_secretkey = None
        self.merchant_id = None
        self.host_name = None
        self.url = None
        self.request_host = None
        self.request_type_method = None
        self.request_target = None
        self.authentication_type = None
        self.key_file_path = None
        self.run_environment = None
        self.key_alias = None
        self.key_password = None
        self.response_code = None
        self.response_message = None
        self.v_c_correlation_id = None
        self.enable_log = None
        self.maximum_size = None
        self.log_directory = None
        self.log_file_name = None
        self.proxy_address = None
        self.proxy_port = None
        self.key_file_name = None
        self.request_json_path_data = None
        self.log = None

    def set_merchant_keyid(self, value):
        if not (value.get('merchant_keyid') is None):
            self.merchant_keyid = value['merchant_keyid']

    def set_merchant_secretkey(self, value):
        if not (value.get('merchant_secretkey') is None):
            self.merchant_secretkey = value['merchant_secretkey']

    def set_key_file_path(self, value):
        if not (value.get('keys_directory') is None):
            self.key_file_path = value['keys_directory']

    def set_log_file_name(self, value):
        if not (value.get('log_file_name') is None or value.get('log_file_name') == ""):
            self.log_file_name = value['log_file_name']
        else:
            self.log_file_name = GlobalLabelParameters.LOG_FILE_NAME_DEFAULT

    def set_key_alias(self, value):
        if not (value.get('key_alias') is None):
            self.key_alias = value['key_alias']

    def set_key_password(self, value):
        if not (value.get('key_password') is None):
            self.key_password = value['key_password']

    def set_authentication_type(self, value):
        if not (value.get('authentication_type') is None):
            self.authentication_type = value['authentication_type']

    def set_merchant_id(self, value):
        if not (value.get('merchantid') is None):
            self.merchant_id = value['merchantid']

    def set_enable_log(self, value):

        if not (value.get('enable_log') == "" or value.get('enable_log') is None):
            self.enable_log = value['enable_log']
        else:
            self.enable_log = GlobalLabelParameters.DEFAULT_ENABLE_LOG

    def set_maximum_size(self, value):

        if not (value.get('log_maximum_size') == "" or value.get('log_maximum_size') is None):
            self.maximum_size = value['log_maximum_size']
        else:
            self.maximum_size = GlobalLabelParameters.DEFAULT_MAXIMUM_SIZE  # 10 MB = 10485760 bytes

    def set_log_directory(self, value):

        if not (value.get('log_directory') == "" or value.get('log_directory') is None):
            if os.path.exists(value['log_directory']) or os.path.isdir(value['log_directory']):
                self.log_directory = value['log_directory']
            else:
                self.log_directory = GlobalLabelParameters.DEFAULT_LOG_DIRECTORY
        else:
            self.log_directory = GlobalLabelParameters.DEFAULT_LOG_DIRECTORY

    def set_run_environment(self, value):
        if not (value.get('run_environment') is None):
            self.run_environment = value['run_environment']

    # setting up hostname based on the run environment value
    def set_request_host(self, value):
        if not (value.get("run_environment") is None):
            if self.run_environment.lower() == GlobalLabelParameters.SANBOX_RUN_ENVIRONMENT.lower():
                self.request_host = GlobalLabelParameters.SANBOX_URL
            elif self.run_environment.lower() == GlobalLabelParameters.PRODUCTION_RUN_ENVIRONMENT.lower():
                self.request_host = GlobalLabelParameters.PRODUCTION_URL
            else:
                self.request_host = self.run_environment

    def set_proxy_address(self, value):
        if not (value.get('proxy_address') is None):
            self.proxy_address = value['proxy_address']

    def set_proxy_port(self, value):
        if not (value.get("proxy_port") is None):
            self.proxy_port = value['proxy_port']

    def set_key_file_name(self, value):
        if not (value.get('key_file_name') is None):
            self.key_file_name = value['key_file_name']

    # This method sets the Merchant Configaration Variables to its respective values after reading from cybs.properties
    def set_merchantconfig(self, val):

        self.set_key_password(val)
        self.set_key_alias(val)
        self.set_key_file_path(val)
        self.set_key_file_name(val)
        self.set_merchant_keyid(val)
        self.set_merchant_secretkey(val)
        self.set_run_environment(val)
        self.set_merchant_id(val)
        self.set_authentication_type(val)
        self.set_enable_log(val)
        self.set_maximum_size(val)
        self.set_log_directory(val)
        self.set_request_host(val)
        self.set_log_file_name(val)
        self.set_proxy_address(val)
        self.set_proxy_port(val)



    # Returns the time in format as defined by RFC7231
    def get_time(self):
        now = datetime.now()
        stamp = mktime(now.timetuple())

        return format_date_time(stamp)

    # This validates the Merchant details
    def validate_merchant_details(self, details, mconfig):
        # verify Mandatory Properties
        logger = cybersource_rest_client_python.authenticationsdk.logger.Log.setup_logger(mconfig)
        mconfig.log = logger
        if self.enable_log is True:
            logger.info("START> ======================================= ")
        if self.merchant_id is None or self.merchant_id == "":
            cybersource_rest_client_python.authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(logger,
                                                                               GlobalLabelParameters.MERCHANTID_REQ,
                                                                               mconfig)

        if self.authentication_type is None or self.authentication_type == "":
            cybersource_rest_client_python.authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(logger,
                                                                               GlobalLabelParameters.AUTHENTICATION_REQ,
                                                                               mconfig)


        if self.run_environment is None or self.run_environment == "":
            cybersource_rest_client_python.authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(logger,
                                                                               GlobalLabelParameters.RUN_ENVIRONMENT_EMPTY,
                                                                               mconfig)

        # Fallback for missing values
        if details.get('enable_log') is None or details.get('enable_log') == "":
            cybersource_rest_client_python.authenticationsdk.util.ExceptionAuth.validate_default_values(logger,
                                                                         GlobalLabelParameters.ENABLE_LOG_DEFAULT_MESSAGE,
                                                                         mconfig)

        if details.get('log_maximum_size') is None or details.get('log_maximum_size') == "":
            cybersource_rest_client_python.authenticationsdk.util.ExceptionAuth.validate_default_values(logger,
                                                                         GlobalLabelParameters.LOG_MAXIMUM_SIZE_DEFAULT_MESSAGE,
                                                                         mconfig)
        if details.get('log_file_name') is None or details.get('log_file_name') == "":
            cybersource_rest_client_python.authenticationsdk.util.ExceptionAuth.validate_default_values(logger,
                                                                         GlobalLabelParameters.DEFAULT_LOG_FILE_NAME,
                                                                         mconfig)

        if details.get('log_directory') is None or details.get('log_directory') == "":
            cybersource_rest_client_python.authenticationsdk.util.ExceptionAuth.validate_default_values(logger,
                                                                         GlobalLabelParameters.LOG_DIRECTORY_DEFAULT_MESSAGE,
                                                                         mconfig)
        elif not (os.path.exists(details.get('log_directory')) or os.path.isdir(details.get('log_directory'))):

            cybersource_rest_client_python.authenticationsdk.util.ExceptionAuth.validate_default_values(logger,
                                                                         GlobalLabelParameters.LOG_DIRECTORY_INCORRECT_MESSAGE,
                                                                         mconfig)

        # This process ensures that merchant_keyid and merchant_secretkey are mandatory in case of HTTP
        # And displays warning if key alias ,key_password,key_filepath,keyfilename are not present when
        # the method is JWT

        if type(self.authentication_type) == str:
            if self.authentication_type.lower() == GlobalLabelParameters.HTTP.lower():
                if self.merchant_keyid is None or self.merchant_keyid == "":
                    cybersource_rest_client_python.authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(logger,
                                                                                       GlobalLabelParameters.MERCHANT_KEY_ID_REQ,
                                                                                       mconfig)

                if self.merchant_secretkey is None or self.merchant_secretkey == "":
                    cybersource_rest_client_python.authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(logger,
                                                                                       GlobalLabelParameters.MERCHANT_SECRET_KEY_REQ,
                                                                                       mconfig)

            elif self.authentication_type.lower() == GlobalLabelParameters.JWT.lower():
                if self.key_alias is None or self.key_alias == "":
                    self.key_alias = self.merchant_id
                    cybersource_rest_client_python.authenticationsdk.util.ExceptionAuth.validate_default_values(logger,
                                                                                 GlobalLabelParameters.KEY_ALIAS_NULL_EMPTY,
                                                                                 mconfig)
                if not (self.key_alias == self.merchant_id):
                    self.key_alias = self.merchant_id
                    cybersource_rest_client_python.authenticationsdk.util.ExceptionAuth.validate_default_values(logger,
                                                                                 GlobalLabelParameters.INVALID_KEY_ALIAS,
                                                                                 mconfig)

                if self.key_password is None or self.key_password == "":
                    self.key_password = self.merchant_id
                    cybersource_rest_client_python.authenticationsdk.util.ExceptionAuth.validate_default_values(logger,
                                                                                 GlobalLabelParameters.KEY_PASSWORD_EMPTY,
                                                                                 mconfig)

                if self.key_file_path is None or self.key_file_path == "":
                    self.key_file_path = GlobalLabelParameters.DEFAULT_KEY_FILE_PATH
                    cybersource_rest_client_python.authenticationsdk.util.ExceptionAuth.validate_default_values(logger,
                                                                                 GlobalLabelParameters.KEY_DIRECTORY_EMPTY + self.key_file_path,
                                                                                 mconfig)

                if self.key_file_name is None or self.key_file_name == "":
                    self.key_file_name = self.merchant_id

                    cybersource_rest_client_python.authenticationsdk.util.ExceptionAuth.validate_default_values(logger,
                                                                                 GlobalLabelParameters.KEY_FILE_EMPTY,
                                                                                 mconfig)
        else:
            cybersource_rest_client_python.authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(logger,
                                                                               GlobalLabelParameters.AUTH_ERROR,
                                                                               mconfig)

        log_items = GlobalLabelParameters.HIDE_MERCHANT_CONFIG_PROPS
        # This displays the logic for logging all cybs.json values
        if self.enable_log is True:
            for key, value in list(details.items()):
                if key in log_items:
                    del details[key]

                for keys, values in list(details.items()):
                    details[keys] = str(values)

            logger.info("Mconfig >      " + str(ast.literal_eval(json.dumps(details))))
