class SoftAssertions:
    def __init__(self):
        self.errors = []

    def assert_equal(self, actual, expected, message=""):
        try:
            assert actual == expected, f"{message} - Expected: {expected}, Actual: {actual}"
            return True  # Assertion passed
        except AssertionError as e:
            self.errors.append(str(e))
            return False  # Assertion failed

    def assert_true(self, condition, message=""):
        try:
            assert condition, f"{message} - Condition is not True"
            return True  # Assertion passed
        except AssertionError as e:
            self.errors.append(str(e))
            return False  # Assertion failed

    def assert_false(self, condition, message=""):
        try:
            assert not condition, f"{message} - Condition is not False"
            return True  # Assertion passed
        except AssertionError as e:
            self.errors.append(str(e))
            return False  # Assertion failed

    def assert_contains(self, container, item, message=""):
        try:
            assert item in container, f"{message} - {item} not found in {container}"
            return True  # Assertion passed
        except AssertionError as e:
            self.errors.append(str(e))
            return False  # Assertion failed

    def assert_not_contains(self, container, item, message=""):
        try:
            assert item not in container, f"{message} - {item} found in {container}"
            return True  # Assertion passed
        except AssertionError as e:
            self.errors.append(str(e))
            return False  # Assertion failed

    def assert_all(self):
        if self.errors:
            raise AssertionError("\n".join(self.errors))