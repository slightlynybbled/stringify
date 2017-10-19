yellow_dot = b'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'
