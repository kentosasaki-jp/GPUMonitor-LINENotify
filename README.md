# GPU Monitor with LINE Notify

**GPU Monitor with LINE Notify** can send `nvidia-smi` information to a LINE channel using LINE Notify.

## Requirement
 ```
 pip install linenotipy
 ```
## Usage
1. Generate **[LINE Notify](https://notify-bot.line.me/en/)** Access Token. 

2. Specify your Access Token.
    ```
    line = Line(token='<Your Access Token>')
    ```

3. Run `monitor.py`

4. Set up a cron job. 

## Reference
GPUmonitorbot. https://github.com/outk/GPUmonitorbot#gpumonitorbot.

