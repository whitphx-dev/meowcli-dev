import argparse


def meow(times: int = 1, emoji: bool = True) -> None:
    for _ in range(times):
        msg = "Meow!"
        if emoji:
            msg = "🐱 " + msg
        print(msg)


def main() -> None:
    parser = argparse.ArgumentParser(description="A cute CLI that meows 🐱")
    parser.add_argument("--times", type=int, default=1, help="Number of times to meow")
    parser.add_argument(
        "--emoji", choices=["on", "off"], default="on", help="Show emoji or not"
    )
    args = parser.parse_args()

    # BUG: emoji=offでも絵文字が出てしまう
    emoji_enabled = args.emoji == "on"  # noqa: F841 - kept for workshop exercise
    meow(times=args.times, emoji=True)  # ← 修正対象
