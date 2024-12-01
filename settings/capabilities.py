from appium.options.android import UiAutomator2Options


class Capabilities:

    @staticmethod
    def get_capabil(capabilities):
        return UiAutomator2Options().load_capabilities(capabilities)
