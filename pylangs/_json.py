import json


class JsonViewer:
    def __str__(self) -> str:
        return json.dumps(
            self,
            ensure_ascii=False,
            indent=2,
            default=lambda x: (
                {k: v for k, v in x.__dict__.items() if (not k.startswith("_")) and v}
            ),
        )
