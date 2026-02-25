<!-- chunk: 2/3 | source: 97j-nicar-2025.md | words: 39289 -->
<!-- headings: Transcribe with WhisperX; First 1500 characters; Comparing transcripts; Download and transcribe many videos; Video processing: Car tracking; Our video; Add detecting; Add tracking; byte_track = sv.ByteTrack(); byte_track.reset(); trace_annotator = sv.TraceAnnotator(); smoother = sv.DetectionsSmoother(); Add counting; line_zone_annotator = sv.LineZoneAnnotator(text_thickness=1); start = sv.Point(200, 175); end = sv.Point(700, 175); line_zone = sv.LineZone(start, end); Final version!; Going further!; \...but also: can we do it with Gemini? -->

## Transcribe with WhisperX

Just like any other AI thing, Whisper isn\'t just one piece of software - it\'s a *collection of models* with different sizes and names that you have to download separately.

You can see [the models here](https://github.com/openai/whisper?tab=readme-ov-file#available-models-and-languages). We\'re going to start with `tiny.en`, an English-only model that is the smallest and fastest.

``` python
%%time

import whisperx
import torch

audio_file = "output.mp3"

device = "cuda" if torch.cuda.is_available() else "cpu"
batch_size = 16 if device == "cuda" else 8
compute_type = "float16" if device == "cuda" else "float32" 

model = whisperx.load_model("tiny.en", device, compute_type=compute_type)

audio = whisperx.load_audio(audio_file)
result = model.transcribe(audio, batch_size=batch_size)
print("Transcribed")

model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)
print("Aligned")
```

    Lightning automatically upgraded your loaded checkpoint from v1.5.4 to v2.0.7. To apply the upgrade to your files permanently, run `python -m pytorch_lightning.utilities.upgrade_checkpoint --file ../../../../../../../../.pyenv/versions/3.10.13/lib/python3.10/site-packages/whisperx/assets/pytorch_model.bin`

    Model was trained with pyannote.audio 0.0.1, yours is 3.3.2. Bad things might happen unless you revert pyannote.audio to 0.x.
    Model was trained with torch 1.10.0+cu102, yours is 2.5.1. Bad things might happen unless you revert torch to 1.x.
    Transcribed
    Aligned
    CPU times: user 3min 52s, sys: 1min 1s, total: 4min 53s
    Wall time: 52.7 s

We can look at the output with timecodes\...

``` python
import pandas as pd

df = pd.json_normalize(result['segments'])
df.head()
```


<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>start</th>
      <th>end</th>
      <th>text</th>
      <th>words</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.271</td>
      <td>2.054</td>
      <td>Hello and welcome to Vancouver Carpenter.</td>
      <td>[{'word': 'Hello', 'start': 0.271, 'end': 0.53...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.634</td>
      <td>7.841</td>
      <td>If you're new to drywall, picking the right mu...</td>
      <td>[{'word': 'If', 'start': 2.634, 'end': 2.694, ...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.881</td>
      <td>12.506</td>
      <td>We've got light mud, we've got all purpose, we...</td>
      <td>[{'word': 'We've', 'start': 7.881, 'end': 8.06...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13.087</td>
      <td>15.090</td>
      <td>So it's hard to know exactly which mud to choose.</td>
      <td>[{'word': 'So', 'start': 13.087, 'end': 13.187...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>15.670</td>
      <td>18.592</td>
      <td>So I'm going to help break that down for you ...</td>
      <td>[{'word': 'So', 'start': 15.67, 'end': 15.87, ...</td>
    </tr>
  </tbody>
</table>


\...or we can just grab the text.

``` python
tiny_en_text = ' '.join([segment['text'] for segment in result['segments']])
print(tiny_en_text)
```

     Hello and welcome to Vancouver Carpenter. If you're new to drywall, picking the right mud can be kind of a daunting task with so many different types. We've got light mud, we've got all purpose, we've got heavyweight, we've got topping, we've got joint. So it's hard to know exactly which mud to choose.  So I'm going to help break that down for you so you can know which one to pick. We're also going to do this in the order that we tape with. So first we're going to start with quick set mugs. So these are the powdered mugs that are bought in bag form. So one of the ones we use a lot here in Western Canada and this isn't available everywhere but it's called concrete fill. So the specific purpose of this mud right here  is actually for skimming out concrete ceilings. So it's got really good adhesion and it's got some light aggregate in it, which I believe is something like pear light. So it's squishy, not like sand.  So that's for skimming out ceilings. It has a really great floatability, but you're not gonna find it everywhere. Hamilton Ultra Fill is another product. It's the same product, basically, just in a different bag from a different company. So we use this for floating big areas, filling large voids. I also use it for jobs where I'm taping with mesh tape. It's a quick setting compound that has about an hour to set. So next, let's get into another quick set. So this one is just your standard 20-minute lead. This is a certain teeth product.  Light sand plus it says light sand because it's supposed to be sandable, but it's not very sandable So this is another product that is suitable for taping with  mesh tape on patches and jobs that you're just not worried about cracking. So this stuff is very hard. It doesn't shrink and I mostly just use it for pre-fill or jobs where I'm trying to get in and out in a day. It sets in about 20 to 30 minutes so you can apply subsequent coats. Now something that most people don't understand about setting muds  They are quick set, not quick drive. If you apply three coats in one day, you still need to wait three or four days for that to drive properly. All it does is allow you to apply a bunch of coats in one day so you don't have to do multiple trips. And it also allows you to do deep fills, like you can fill things up to easily half inch deep, if not deeper, without it shrinking and cracking. So it doesn't do all the weird things that regular mud will do.  So once you've done your pre-filling, the next thing to go on to is some sort of a taping mud. So here in Canada we have what's called light taping mud. So this one says light weight taping.  And this box here is also a taping mud. So in Canada, all of our mud is light. So what that means is in the states, there's actually heavyweight mud. And we'll get into that a little bit when I get into all purpose. So this mud is specifically for laying paper tape. It doesn't coat nicely. It gets bubbles.  And it shrinks a lot and it's harder to sand. So it's specifically for laying tape. It has tons of glue in it. And because it's light, it's not too heavy if you're using, say, automatic taping tools or just carrying around a pan of mud is not too heavy. So next we're going to get into all purpose months. So right here, I have light all purpose.  So it's important to make a distinction. I've been saying light a lot and that's because pretty much all mods up here in Canada are light. And what that means is I'm not sure when they stopped using the regular heavyweight formula and switched over to light. It was maybe in the 80s or 90s.  But a heavyweight mud like your regular sheet rock green lid, USG or your pro form black lid, these mugs that you guys have down in the States that is a regular heavyweight mud is literally twice the weight. You lift up a bucket of  that. If you're a Canadian and you go to pick up a bucket of heavyweight and you've been lifting lightweight buckets your whole life you're gonna oh my goodness because this stuff is just heavy it's a totally different beast and a lot of the time I've been on drywall forms where Canadian tapers are giving the Americans a really hard time. What are you taping with all purpose for?  The thing is, us Canadians don't know that in the states there's a lot of places that don't have taping mud and they don't have light mud. They only have this all-purpose stuff. It's a real bear to work with. It stands horribly, so it's a totally different animal than the light muds we have up here in Canada. Very sticky and very strong.  So let's get into the Canadian lightweight all purpose. So you can tape with it, but it is not as good as a regular mud. So I'd say a light all purpose mud for taping is good enough to give the customer a tailgate warranty. And what that means is when you can't see the tailgate of the contractor anymore, your warranty is expired.  So I carry this stuff around because it's all right for taping things like inside corners and it's good for taping things in a pinch and it also has better adhesion over say glossy paints and things like that than your classic finish. All purpose mud is also one of the only things you should be coating steel beads with.  The real question is, why are you still installing steel beads? So next let's get into finished muds. So right here we've got a classic finish, which just means it's a topping mud. So this mud is not suitable for taping. It is not suitable for coating steel or vinyl beads. But what it is suitable for is getting nice smooth coats with relatively few bubbles on your first coat. And it polishes out really nicely on your final coat. It's also easier to sand.  So in terms of hardness of sanding, taping and the heavyweight all purpose, you don't want to sand that stuff. Light all purpose is pretty darn easy to sand. A comparable product in the States would be USG plus 3. That's a light all purpose. But this stuff is very easy to sand.  If you use a coarse grit of sandpaper like a 120 or sometimes even a 150 on a finish mud, you're going to scratch the crap out of it. So it's very easy to sand, but that also means that you need to be more careful with it when sanding and that it's not going to leave as durable a finish on the customer's wall.  Although in all honesty, we're talking about drywall, not plaster concrete. No matter what drywall you're using, it's going to leave a cheap finish on the wall because drywall's a cheap product, but that's a whole other debate. So the ideal scenario for using something like an all-purpose is when you're doing a really small job like a bunch of patches or a small bathroom.  So you're going to use mesh tape and quick set on your flats and your butt joints and you're going to use paper tape and all purpose for your inside corners. I would probably also install my corner beads with quick set and you're going to get a first coat on everything and a coat on your inside corners with the all purpose and then you're going to do a finished coat with the all purpose.  So it's handy to have if you don't want to carry two different buckets around. You just want one bucket for one job. So for large jobs, what I like to have is I like to have a bag called fill for the deep fills and for pre-filling everything. I like to have taping mud and paper tape because it's the strongest and longest lasting. And then I like to have finished mud because it spreads the nicest and because I get the least pinholes and it sands easily.  So this is for big jobs and then the quick set and then all purpose for the little jobs. So I hope that helps answer some of your questions if you've been wondering about what are all these different types of drywall mods and maybe get a little overwhelmed when you're at the Home Depot. So thanks for watching. See you in the next video.

Around one minute to transcribe 7 minutes of audio. Not awful, I guess!

Whisper models go all the way up to **large-v3**, but it\'s pretty slow! OpenAI recommends you use their new-ish **turbo** model, which is just about as good as the large models but much much faster.

``` python
%%time

import whisperx
import torch

audio_file = "output.mp3"

device = "cuda" if torch.cuda.is_available() else "cpu"
batch_size = 16 if device == "cuda" else 8
compute_type = "float16" if device == "cuda" else "float32" 

model = whisperx.load_model("turbo", device, compute_type=compute_type)

audio = whisperx.load_audio(audio_file)
result = model.transcribe(audio, batch_size=batch_size)
print("Transcribed")

model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)
print("Aligned")
```

    No language specified, language will be first be detected for each audio file (increases inference time).

    Lightning automatically upgraded your loaded checkpoint from v1.5.4 to v2.0.7. To apply the upgrade to your files permanently, run `python -m pytorch_lightning.utilities.upgrade_checkpoint --file ../../../../../../../../.pyenv/versions/3.10.13/lib/python3.10/site-packages/whisperx/assets/pytorch_model.bin`

    Model was trained with pyannote.audio 0.0.1, yours is 3.3.2. Bad things might happen unless you revert pyannote.audio to 0.x.
    Model was trained with torch 1.10.0+cu102, yours is 2.5.1. Bad things might happen unless you revert torch to 1.x.
    Detected language: en (1.00) in first 30s of audio...
    Transcribed
    Aligned
    CPU times: user 7min 13s, sys: 2min, total: 9min 13s
    Wall time: 2min 19s

It took two minutes on the \"turbo\" setting.

``` python
turbo_text = ' '.join([segment['text'] for segment in result['segments']])

# First 1500 characters
print(turbo_text[:1500])
```

     Hello and welcome to Vancouver Carpenter. If you're new to drywall, picking the right mud can be kind of a daunting task with so many different types. We've got light mud, we've got all purpose, we've got heavy weight, we've got topping, we've got joint. So it's hard to know exactly which mud to choose.  So, I'm going to help break that down for you so you can know which one to pick. We're also going to do this in the order that we tape with. So, first we're going to start with quick set muds. So, these are the powdered mugs that are bought in bag form. So, one of the ones we use a lot here in Western Canada, and this isn't available everywhere, but it's called concrete fill. So, the specific purpose of this mud, right here,  is actually for skimming out concrete ceilings. So it's got really good adhesion and it's got some light aggregate in it, which I believe is something like perlite. So it's squishy, not like sand.  So that's for skimming out ceilings. It has really great floatability, but you're not going to find it everywhere. Hamilton Ultra Fill is another product. It's the same product, basically, just in a different bag from a different company. So we use this for floating big areas, filling large voids. I also use it for jobs where I'm taping with mesh tape. It's a quick setting compound that has about an hour to set. So next, let's get into another quick set. So this one is just your standard 20 minute mud. This is a CertainTeed product.  light sand plus it says l


## Comparing transcripts

There\'s no good comparison library in Python! I like to just throw files into [VS Code](https://code.visualstudio.com/) and do it manually, but we\'ll do a little DIY situation to compare here.

``` python
%pip install --quiet --upgrade rich diff_match_patch
```

    ^C
    ERROR: Operation cancelled by user
    Note: you may need to restart the kernel to use updated packages.

``` python
from rich.console import Console
from rich.markup import escape
from diff_match_patch import diff_match_patch

console = Console(record=True, width=100)

def pretty_diff_rich(text1, text2):
    dmp = diff_match_patch()
    diffs = dmp.diff_main(text1, text2)
    dmp.diff_cleanupSemantic(diffs)  # Clean up to make the diff more readable

    formatted_output = []
    for op, text in diffs:
        safe_text = escape(text)  # Prevent issues with brackets in Rich

        if op == -1:
            formatted_output.append(f"black on #ffcccc[/black on #ffcccc]")  # Light red background for deletions
        elif op == 1:
            formatted_output.append(f"black on #ccffcc[/black on #ccffcc]")  # Light green background for additions
        else:
            formatted_output.append(safe_text)  # Normal text

    console.print("".join(formatted_output))


pretty_diff_rich(tiny_en_text, turbo_text)
```

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"> Hello and welcome to Vancouver Carpenter. If you're new to drywall, picking the right mud can be 
kind of a daunting task with so many different types. We've got light mud, we've got all purpose, 
we've got heavy weight, we've got topping, we've got joint. So it's hard to know exactly which mud 
to choose.  So, I'm going to help break that down for you so you can know which one to pick. We're 
also going to do this in the order that we tape with. So, first we're going to start with quick set 
mugds. So, these are the powdered mugs that are bought in bag form. So, one of the ones we use a lot
here in Western Canada, and this isn't available everywhere, but it's called concrete fill. So, the 
specific purpose of this mud, right here,  is actually for skimming out concrete ceilings. So it's 
got really good adhesion and it's got some light aggregate in it, which I believe is something like 
pear lightrlite. So it's squishy, not like sand.  So that's for skimming out ceilings. It has a 
really great floatability, but you're not gonnaing to find it everywhere. Hamilton Ultra Fill is 
another product. It's the same product, basically, just in a different bag from a different company.
So we use this for floating big areas, filling large voids. I also use it for jobs where I'm taping 
with mesh tape. It's a quick setting compound that has about an hour to set. So next, let's get into
another quick set. So this one is just your standard 20- minute leamud. This is a cCertain teethTeed
product.  Llight sand plus it says light sand because it's supposed to be sandable, but it's not 
very sandable Sso this is another product that is suitable for taping with  mesh tape on patches and
jobs that you're just not worried about cracking. So this stuff is very hard. I, it doesn't shrink, 
and I mostly just use it for pre-fill or jobs where I'm trying to get in and out in a day. It sets 
in about 20 to 30 minutes so you can apply subsequent coats. Now, something that most people don't 
understand about setting muds  They are quick set, not quick drivey. If you apply three coats in one
day, you still need to wait three or four days for that to drivey properly. All it does is allow you
to apply a bunch of coats in one day so you don't have to do multiple trips. And it also allows you 
to do deep fills, like you can fill things up to easily half inch deep, if not deeper, without it 
shrinking and cracking. So it doesn't do all the weird things that regular mud will do.  So once 
you've done your pre-filling, the next thing to go on to is some sort of a taping mud. So here in 
Canada we have what's called light taping mud. So this one says light weight taping.  And this box 
here is also a taping mud. So in Canada, all of our mud is light. So what that means is in the 
sStates, there's actually heavyweight mud. And we'll get into that a little bit when I get into aAll
pPurpose. So this mud is specifically for laying paper tape. It doesn't coat nicely. It gets 
bubbles.  Aand it shrinks a lot and it's harder to sand. S so it's specifically for laying tape. I 
it has tons of glue in it. A and because it's light, it's not too heavy if you're using, say, 
automatic taping tools or just carrying around a pan of mud it's not too heavy. S so next we're 
going to get into all -purpose months. Sud so right here, I i have light all -purpose.  So it's 
important to make a distinction. I've been saying light a lot and that's because pretty much all 
mouds up here in Canada are light. And what that means is I'm not sure when they stopped using the 
regular heavyweight formula and switched over to light. It was maybe in the 80s or 90s.  Bbut a 
heavyweight mud like your regular sheet rock green lid, USG or your pro form black lid, these mugds 
that you guys have down in the Sstates that is a regular heavyweight mud is literally twice the 
weight. Y you lift up a bucket of  that. If you're a Canadian and you go to pick up a bucket of 
heavy weight and you've been lifting lightweight buckets your whole life, you're gonnaing to, oh my 
goodness, because this stuff is just heavy i. It's a totally different beast a. And a lot of the 
time I've been on drywall forums where Canadian tapers are giving the Americans a really hard time. 
What are you taping with all purpose for?  Tthe thing is, us Canadians don't know that in the states
there's a lot of places that don't have taping mud and they don't have light mud. T they only have 
this all-purpose stuff. I it's a real bear to work with. I it stands horribly, so it's a totally 
different animal than the light muds we have up here in Canada. V very sticky and very strong.  So 
let's get into the Canadian lightweight all -purpose. So you can tape with it, but it is not as good
as a regular mud. So I'd say a light all -purpose mud for taping is good enough to give the customer
a tailgate warranty. And what that means is when you can't see the tailgate of the contractor 
anymore, your warranty is expired.  So I carry this stuff around because it's all right for taping 
things like inside corners and it's good for taping things in a pinch and it also has better 
adhesion over say glossy paints and things like that than your classic finish. All purpose mud is 
also one of the only things you should be coating steel beads with.  The real question is, why are 
you still installing steel beads? So next let's get into finished muds. So right here we've got a 
classic finish, which just means it's a topping mud. So this mud is not suitable for taping. I, it 
is not suitable for coating steel or vinyl beads. B, but what it is suitable for is getting nice 
smooth coats with relatively few bubbles on your first coat. A and it polishes out really nicely on 
your final coat. It's also easier to sand.  So in terms of hardness of sanding, taping and the 
heavyweight all -purpose, you don't want to sand that stuff. Light all -purpose is pretty darn easy 
to sand. A comparable product in the States would be USG plus 3. That's a light all -purpose. But 
this stuff is very easy to sand.  If you use a coarse grit of sandpaper like a 120 or sometimes even
a 150 on a finished mud, you're going to scratch the crap out of it. So it's very easy to sand, but 
that also means that you need to be more careful with it when sanding and that it's not going to 
leave as durable a finish on the customer's wall.  Although in all honesty, we're talking about 
drywall, not plaster or concrete. No matter what drywall you're using, it's going to leave a cheap 
finish on the wall because drywall' is a cheap product, but that's a whole other debate. So the 
ideal scenario for using something like an all-purpose is when you're doing a really small job like 
a bunch of patches or a small bathroom.  So you're going to use mesh tape and quick set on your 
flats and your butt joints and you're going to use paper tape and all purpose for your inside 
corners. I would probably also install my corner beads with quick set and you're going to get a 
first coat on everything and a coat on your inside corners with the all purpose and then you're 
going to do a finished coat with the all purpose.  So it's handy to have if you don't want to carry 
two different buckets around. You just want one bucket for one job. So for large jobs, what I like 
to have is I like to have a bag calledof con fill for the deep fills and for pre-filling everything.
I like to have taping mud and paper tape because it's the strongest and longest lasting. And then I 
like to have finished mud because it spreads the nicest and because I get the least pinholes and it 
sands easily.  Sso this is for big jobs and then the quick set and then all -purpose for the little 
jobs. S so Ii hope that helps answer some of your questions if you've been wondering about what are 
all these different types of drywall mouds and maybe you get a little overwhelmed when you're at the
Hhome Ddepot. S so thanks for watching. S see you in the next video.
</pre>

# Download and transcribe many videos

``` python
import pandas as pd

urls = [
    'eIK50QLHpOc',
    's-4yh3XY5wU',
    'T4g-OBXCy1k',
    'GIvmfBuAQIw',
    'CzrnOujf8YA'
]
df = pd.DataFrame({'video_id': urls})
df['url'] = 'https://www.youtube.com/watch?v=' + df['video_id']
df
```


<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>video_id</th>
      <th>url</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>eIK50QLHpOc</td>
      <td>https://www.youtube.com/watch?v=eIK50QLHpOc</td>
    </tr>
    <tr>
      <th>1</th>
      <td>s-4yh3XY5wU</td>
      <td>https://www.youtube.com/watch?v=s-4yh3XY5wU</td>
    </tr>
    <tr>
      <th>2</th>
      <td>T4g-OBXCy1k</td>
      <td>https://www.youtube.com/watch?v=T4g-OBXCy1k</td>
    </tr>
    <tr>
      <th>3</th>
      <td>GIvmfBuAQIw</td>
      <td>https://www.youtube.com/watch?v=GIvmfBuAQIw</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CzrnOujf8YA</td>
      <td>https://www.youtube.com/watch?v=CzrnOujf8YA</td>
    </tr>
  </tbody>
</table>


``` python
from yt_dlp import YoutubeDL
from pathlib import Path

download_dir = Path("downloads")

video_dir = download_dir / video_dir
audio_dir = download_dir / audio_dir

video_dir.mkdir(exist_ok=True, parents=True)
audio_dir.mkdir(exist_ok=True, parents=True)

video_opts = {
    'format': 'bestvideo[height<=720]+bestaudio',
    'outtmpl': str(video_dir / '%(id)s.%(ext)s'),  # Using / operator for paths
    'quiet': True,
    'ignoreerrors': True,
    'no_warnings': False
}

audio_opts = {
    'format': 'bestaudio',
    'outtmpl': str(audio_dir / '%(id)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'quiet': False,
    'ignoreerrors': True
}

try:
    with YoutubeDL(audio_opts) as ydl:
        ydl.download(df.url)
except Exception as e:
    print(f"Error during download: {e}")
```

    [youtube] Extracting URL: https://www.youtube.com/watch?v=eIK50QLHpOc
    [youtube] eIK50QLHpOc: Downloading webpage
    [youtube] eIK50QLHpOc: Downloading tv client config
    [youtube] eIK50QLHpOc: Downloading player 9c6dfc4a
    [youtube] eIK50QLHpOc: Downloading tv player API JSON
    [youtube] eIK50QLHpOc: Downloading ios player API JSON
    [youtube] eIK50QLHpOc: Downloading m3u8 information
    [info] eIK50QLHpOc: Downloading 1 format(s): 251
    [download] Destination: downloads/downloads/audio/eIK50QLHpOc.webm
    [download] 100% of    2.16MiB in 00:00:00 at 7.05MiB/s   
    [ExtractAudio] Destination: downloads/downloads/audio/eIK50QLHpOc.mp3
    Deleting original file downloads/downloads/audio/eIK50QLHpOc.webm (pass -k to keep)
    [youtube] Extracting URL: https://www.youtube.com/watch?v=s-4yh3XY5wU
    [youtube] s-4yh3XY5wU: Downloading webpage
    [youtube] s-4yh3XY5wU: Downloading tv client config
    [youtube] s-4yh3XY5wU: Downloading tv player API JSON
    [youtube] s-4yh3XY5wU: Downloading ios player API JSON
    [youtube] s-4yh3XY5wU: Downloading m3u8 information
    [info] s-4yh3XY5wU: Downloading 1 format(s): 251
    [download] Destination: downloads/downloads/audio/s-4yh3XY5wU.webm
    [download] 100% of    5.21MiB in 00:00:00 at 8.29MiB/s   
    [ExtractAudio] Destination: downloads/downloads/audio/s-4yh3XY5wU.mp3
    Deleting original file downloads/downloads/audio/s-4yh3XY5wU.webm (pass -k to keep)
    [youtube] Extracting URL: https://www.youtube.com/watch?v=T4g-OBXCy1k
    [youtube] T4g-OBXCy1k: Downloading webpage
    [youtube] T4g-OBXCy1k: Downloading tv client config
    [youtube] T4g-OBXCy1k: Downloading tv player API JSON
    [youtube] T4g-OBXCy1k: Downloading ios player API JSON
    [youtube] T4g-OBXCy1k: Downloading m3u8 information
    [info] T4g-OBXCy1k: Downloading 1 format(s): 251
    [download] Destination: downloads/downloads/audio/T4g-OBXCy1k.webm
    [download] 100% of    1.25MiB in 00:00:00 at 4.67MiB/s   
    [ExtractAudio] Destination: downloads/downloads/audio/T4g-OBXCy1k.mp3
    Deleting original file downloads/downloads/audio/T4g-OBXCy1k.webm (pass -k to keep)
    [youtube] Extracting URL: https://www.youtube.com/watch?v=GIvmfBuAQIw
    [youtube] GIvmfBuAQIw: Downloading webpage
    [youtube] GIvmfBuAQIw: Downloading tv client config
    [youtube] GIvmfBuAQIw: Downloading tv player API JSON
    [youtube] GIvmfBuAQIw: Downloading ios player API JSON
    [youtube] GIvmfBuAQIw: Downloading m3u8 information
    [info] GIvmfBuAQIw: Downloading 1 format(s): 251
    [download] Destination: downloads/downloads/audio/GIvmfBuAQIw.webm
    [download] 100% of    4.54MiB in 00:00:00 at 8.67MiB/s   
    [ExtractAudio] Destination: downloads/downloads/audio/GIvmfBuAQIw.mp3
    Deleting original file downloads/downloads/audio/GIvmfBuAQIw.webm (pass -k to keep)
    [youtube] Extracting URL: https://www.youtube.com/watch?v=CzrnOujf8YA
    [youtube] CzrnOujf8YA: Downloading webpage
    [youtube] CzrnOujf8YA: Downloading tv client config
    [youtube] CzrnOujf8YA: Downloading tv player API JSON
    [youtube] CzrnOujf8YA: Downloading ios player API JSON
    [youtube] CzrnOujf8YA: Downloading m3u8 information
    [info] CzrnOujf8YA: Downloading 1 format(s): 251
    [download] Destination: downloads/downloads/audio/CzrnOujf8YA.webm
    [download] 100% of    3.26MiB in 00:00:00 at 9.58MiB/s   
    [ExtractAudio] Destination: downloads/downloads/audio/CzrnOujf8YA.mp3
    Deleting original file downloads/downloads/audio/CzrnOujf8YA.webm (pass -k to keep)

``` python
df['audio_path'] = "downloads/audio/" + df['video_id'] + ".mp3"
df
```


<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>video_id</th>
      <th>url</th>
      <th>audio_path</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>eIK50QLHpOc</td>
      <td>https://www.youtube.com/watch?v=eIK50QLHpOc</td>
      <td>downloads/audio/eIK50QLHpOc.mp3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>s-4yh3XY5wU</td>
      <td>https://www.youtube.com/watch?v=s-4yh3XY5wU</td>
      <td>downloads/audio/s-4yh3XY5wU.mp3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>T4g-OBXCy1k</td>
      <td>https://www.youtube.com/watch?v=T4g-OBXCy1k</td>
      <td>downloads/audio/T4g-OBXCy1k.mp3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>GIvmfBuAQIw</td>
      <td>https://www.youtube.com/watch?v=GIvmfBuAQIw</td>
      <td>downloads/audio/GIvmfBuAQIw.mp3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CzrnOujf8YA</td>
      <td>https://www.youtube.com/watch?v=CzrnOujf8YA</td>
      <td>downloads/audio/CzrnOujf8YA.mp3</td>
    </tr>
  </tbody>
</table>


``` python
%%time
import whisperx
import torch

from tqdm.notebook import tqdm
tqdm.pandas()

device = "cuda" if torch.cuda.is_available() else "cpu"
batch_size = 16 if device == "cuda" else 4
compute_type = "float16" if device == "cuda" else "int8" 

model = whisperx.load_model("tiny.en", device, compute_type=compute_type)

def get_text(video_id):
    try:
        audio_file = f"downloads/audio/{video_id}.mp3"
        audio = whisperx.load_audio(audio_file)
        result = model.transcribe(audio, batch_size=batch_size)
        
        model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
        result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)
        
        text = '\n'.join([segment['text'] for segment in result['segments']])
        return text
    except Exception as e:
        print(f"Error with {video_id}: {e}")
        return None

df['text'] = df.video_id.progress_apply(get_text)
```

    Lightning automatically upgraded your loaded checkpoint from v1.5.4 to v2.0.7. To apply the upgrade to your files permanently, run `python -m pytorch_lightning.utilities.upgrade_checkpoint --file ../../../../../../../.pyenv/versions/3.10.13/lib/python3.10/site-packages/whisperx/assets/pytorch_model.bin`

    Model was trained with pyannote.audio 0.0.1, yours is 3.3.2. Bad things might happen unless you revert pyannote.audio to 0.x.
    Model was trained with torch 1.10.0+cu102, yours is 2.5.1. Bad things might happen unless you revert torch to 1.x.

``` json
{"model_id":"2b6d44281a0643ec8eb186c8b28abc72","version_major":2,"version_minor":0}
```

    CPU times: user 12min 54s, sys: 2min 52s, total: 15min 46s
    Wall time: 2min 32s


<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>video_id</th>
      <th>url</th>
      <th>audio_path</th>
      <th>text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>eIK50QLHpOc</td>
      <td>https://www.youtube.com/watch?v=eIK50QLHpOc</td>
      <td>downloads/audio/eIK50QLHpOc.mp3</td>
      <td>Welcome to Vancouver Carpenter.\nSo are those...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>s-4yh3XY5wU</td>
      <td>https://www.youtube.com/watch?v=s-4yh3XY5wU</td>
      <td>downloads/audio/s-4yh3XY5wU.mp3</td>
      <td>Hello and welcome to Vancouver Carpenter.\nIf...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>T4g-OBXCy1k</td>
      <td>https://www.youtube.com/watch?v=T4g-OBXCy1k</td>
      <td>downloads/audio/T4g-OBXCy1k.mp3</td>
      <td>Welcome back to Vancouver Carpenter.\nSo I ge...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>GIvmfBuAQIw</td>
      <td>https://www.youtube.com/watch?v=GIvmfBuAQIw</td>
      <td>downloads/audio/GIvmfBuAQIw.mp3</td>
      <td>Hello and welcome to Vancouver Carpenter.\nSo...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CzrnOujf8YA</td>
      <td>https://www.youtube.com/watch?v=CzrnOujf8YA</td>
      <td>downloads/audio/CzrnOujf8YA.mp3</td>
      <td>Welcome to Vancouver Carpenter.\nToday's vide...</td>
    </tr>
  </tbody>
</table>


``` python
df.head()
```


<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>video_id</th>
      <th>url</th>
      <th>audio_path</th>
      <th>text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>eIK50QLHpOc</td>
      <td>https://www.youtube.com/watch?v=eIK50QLHpOc</td>
      <td>downloads/audio/eIK50QLHpOc.mp3</td>
      <td>Welcome to Vancouver Carpenter.\nSo are those...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>s-4yh3XY5wU</td>
      <td>https://www.youtube.com/watch?v=s-4yh3XY5wU</td>
      <td>downloads/audio/s-4yh3XY5wU.mp3</td>
      <td>Hello and welcome to Vancouver Carpenter.\nIf...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>T4g-OBXCy1k</td>
      <td>https://www.youtube.com/watch?v=T4g-OBXCy1k</td>
      <td>downloads/audio/T4g-OBXCy1k.mp3</td>
      <td>Welcome back to Vancouver Carpenter.\nSo I ge...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>GIvmfBuAQIw</td>
      <td>https://www.youtube.com/watch?v=GIvmfBuAQIw</td>
      <td>downloads/audio/GIvmfBuAQIw.mp3</td>
      <td>Hello and welcome to Vancouver Carpenter.\nSo...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CzrnOujf8YA</td>
      <td>https://www.youtube.com/watch?v=CzrnOujf8YA</td>
      <td>downloads/audio/CzrnOujf8YA.mp3</td>
      <td>Welcome to Vancouver Carpenter.\nToday's vide...</td>
    </tr>
  </tbody>
</table>


``` python
```



## Video processing: Car tracking

Want to reproduce [this Bloomberg piece about congestion pricing?](https://www.bloomberg.com/graphics/2025-nyc-congestion-pricing-week-one-traffic-mix-shifts/) We can get about\... 60% of the way there!

This code is based heavily on [Piotr Skalski\'s presentation](https://x.com/i/broadcasts/1YqKDkdMOOYxV) at MIT from Nov 14, 2024. His is a good bit more interesting, though, as it talks about extracting license plates, OCRing them and tracking their movement in and out of a parking lot.

The library we\'re using for most of this is [supervision](https://supervision.roboflow.com/latest/), which is very very very tied to [Roboflow](https://roboflow.com/). Think of Roboflow as the the Hugging Face of vision models, except Hugging Face *does* have vision models and Roboflow\'s website is *not that easy to use*. Supervision is a fantastic library, though, so we\'re using it!

> If you want to use Hugging Face + pipelines + whatever models from over there, you just need to convert your detects into a supervision-friendly format. I just print out what my model gives me and ask an LLM.


## Our video

We\'re starting from a wonderful video from iStockPhoto because I don\'t have a bunch of videos of traffic laying around (sorry).

<video src="istockphoto-534232220-640_adpp_is.mp4" controls loop autoplay>

Let\'s see what we can do with it!



## Add detecting

``` python
from IPython.display import clear_output, display
from PIL import Image
import os
import time
import supervision as sv
from inference import get_model

model = get_model("yolov10n-640")

video_path = "istockphoto-534232220-640_adpp_is.mp4"
frame_generator = sv.get_video_frames_generator(video_path)

box_annotator = sv.BoxAnnotator()
label_annotator = sv.LabelAnnotator()

try:
    for frame in frame_generator:
        result = model.infer(frame)[0]
        detections = sv.Detections.from_inference(result)

        annotated_frame = frame.copy()
        
        annotated_frame = box_annotator.annotate(annotated_frame, detections)
    
        annotated_frame = label_annotator.annotate(
            scene=annotated_frame,
            detections=detections)
    
        # Display the image
        clear_output(wait=True)
        display(Image.fromarray(annotated_frame))
except KeyboardInterrupt:
    print("Exiting")
```

    Exiting


## Add tracking

``` python
from IPython.display import clear_output, display
from PIL import Image
import os
import time
import supervision as sv
from inference import get_model

model = get_model("yolov10n-640")

video_path = "istockphoto-534232220-640_adpp_is.mp4"
frame_generator = sv.get_video_frames_generator(video_path)

box_annotator = sv.BoxAnnotator()
label_annotator = sv.LabelAnnotator()

# byte_track = sv.ByteTrack()
# byte_track.reset()

# trace_annotator = sv.TraceAnnotator()
# smoother = sv.DetectionsSmoother()

try:
    for frame in frame_generator:
        result = model.infer(frame, confidence=0.3)[0]
        detections = sv.Detections.from_inference(result)
        # detections = byte_track.update_with_detections(detections)
        # detections = smoother.update_with_detections(detections)
        
        annotated_frame = frame.copy()
        labels = [
            f"{model.class_names[class_id]} {confidence:0.2f}"
            for _, _, confidence, class_id, tracker_id, _
            in detections
        ]
        
        annotated_frame = box_annotator.annotate(annotated_frame, detections)
        # annotated_frame = trace_annotator.annotate(annotated_frame, detections)
    
        annotated_frame = label_annotator.annotate(
            scene=annotated_frame,
            detections=detections,
            labels=labels)
    
        # Display the image
        clear_output(wait=True)
        display(Image.fromarray(annotated_frame))
except KeyboardInterrupt:
    print("Exiting")
```


    Exiting



## Add counting

``` python
from IPython.display import clear_output, display
from PIL import Image
import os
import time
import supervision as sv
from inference import get_model

model = get_model("yolov10n-640")

video_path = "istockphoto-534232220-640_adpp_is.mp4"
frame_generator = sv.get_video_frames_generator(video_path)

box_annotator = sv.BoxAnnotator()
label_annotator = sv.LabelAnnotator()
# line_zone_annotator = sv.LineZoneAnnotator(text_thickness=1)

byte_track = sv.ByteTrack()
byte_track.reset()

# start = sv.Point(200, 175)
# end = sv.Point(700, 175)
# line_zone = sv.LineZone(start, end)
trace_annotator = sv.TraceAnnotator()
smoother = sv.DetectionsSmoother()

try:
    for frame in frame_generator:
        result = model.infer(frame, confidence=0.3)[0]
        detections = sv.Detections.from_inference(result)
        detections = byte_track.update_with_detections(detections)
        detections = smoother.update_with_detections(detections)
    
        # line_zone.trigger(detections)
    
        annotated_frame = frame.copy()
        labels = [
            f"#{tracker_id} {model.class_names[class_id]} {confidence:0.2f}"
            for _, _, confidence, class_id, tracker_id, _
            in detections
        ]
        
        annotated_frame = box_annotator.annotate(annotated_frame, detections)
        annotated_frame = trace_annotator.annotate(annotated_frame, detections)
    
        annotated_frame = label_annotator.annotate(
            scene=annotated_frame,
            detections=detections,
            labels=labels)
    
        # annotated_frame = line_zone_annotator.annotate(
        #     annotated_frame,
        #     line_counter=line_zone)
    
        # Display the image
        clear_output(wait=True)
        display(Image.fromarray(annotated_frame))
except KeyboardInterrupt:
    print("Exiting")
```

    Exiting


## Final version!

``` python
from IPython.display import clear_output, display
from PIL import Image
import os
import time
import supervision as sv
from inference import get_model

model = get_model("yolov10n-640")

video_path = "istockphoto-534232220-640_adpp_is.mp4"
frame_generator = sv.get_video_frames_generator(video_path)

box_annotator = sv.BoxAnnotator()
label_annotator = sv.LabelAnnotator()
line_zone_annotator = sv.LineZoneAnnotator(text_thickness=1)

byte_track = sv.ByteTrack()
byte_track.reset()

start = sv.Point(200, 175)
end = sv.Point(700, 175)
line_zone = sv.LineZone(start, end)
trace_annotator = sv.TraceAnnotator()
smoother = sv.DetectionsSmoother()

try:
    for frame in frame_generator:
        result = model.infer(frame, confidence=0.3)[0]
        detections = sv.Detections.from_inference(result)
        detections = byte_track.update_with_detections(detections)
        detections = smoother.update_with_detections(detections)
    
        line_zone.trigger(detections)
    
        annotated_frame = frame.copy()
        labels = [
            f"#{tracker_id} {model.class_names[class_id]} {confidence:0.2f}"
            for _, _, confidence, class_id, tracker_id, _
            in detections
        ]
        
        annotated_frame = box_annotator.annotate(annotated_frame, detections)
        annotated_frame = trace_annotator.annotate(annotated_frame, detections)
    
        annotated_frame = label_annotator.annotate(
            scene=annotated_frame,
            detections=detections,
            labels=labels)
    
        annotated_frame = line_zone_annotator.annotate(
            annotated_frame,
            line_counter=line_zone)
    
        # Display the image
        clear_output(wait=True)
        display(Image.fromarray(annotated_frame))
except KeyboardInterrupt:
    print("Exiting")
```




## Going further!

What if you don\'t just want cars, though -- you want to be *Bloomberg*, and spot taxis and box trucks and commercial vehicles and all sorts of specific cars! While you might try to find a model that does that for you, you can also **train your own** with a handful of pictures and videos.

If you\'re interested in going to the next level instead of just using out-of-the-box models, check out [the Roboflow documentation](https://blog.roboflow.com/getting-started-with-roboflow/).

# \...but also: can we do it with Gemini?

We\'re going to steal the code from [the video understanding notebook](01-Video%20understanding%20with%20Google%20Gemini.ipynb) and see how it does.

``` python
from google import genai
from google.genai import types

client = genai.Client(api_key='AIzaSyD--gLjge7h1wXqL3wRnIG1HskVS_JkrJo')
```

``` python
def upload_video(video_file_name):
  video_file = client.files.upload(file=video_file_name)

  while video_file.state == "PROCESSING":
      print('Waiting for video to be processed.')
      time.sleep(10)
      video_file = client.files.get(name=video_file.name)

  if video_file.state == "FAILED":
    raise ValueError(video_file.state)
  print(f'Video processing complete: ' + video_file.uri)

  return video_file
```

``` python
video = upload_video("istockphoto-534232220-640_adpp_is.mp4")
```

    Waiting for video to be processed.
    Video processing complete: https://generativelanguage.googleapis.com/v1beta/files/soibszmj3xx9

``` python
from IPython.display import display, Markdown, HTML
from google.genai.types import GenerateContentConfig

prompt = """
Watch the traffic video. Provide a count of the number of cars that 
go into the left tunnel and the number of cars that come out of 
the right tunnel.
"""

video = video

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[
        video,
        prompt,
    ],
    config=GenerateContentConfig(temperature=0)
)

print(response.text)
```

    Okay, I've watched the video.

    *   **Cars entering the left tunnel:** 10
    *   **Cars exiting the right tunnel:** 12

**The actual number is around 20 and 20,** so no! Let\'s maybe not trust the all-knowing AI with this one.

``` python
```


## Setup and installation

Avoid setup and just [use these notebooks on Google Colab](http://colab.research.google.com/github/jsoma/nicar25-ai-images-video/).

### NICAR computer setup instructions you can use

Open up **Terminal** (it's a little black box down at the bottom of the screen), copy and paste this and hit enter:

```
cd ~/Desktop/hands_on_classes/20250307-friday-analyzing-images-and-videos-with-ai
source env/bin/activate
jupyter notebook
```

It should open up a browser with some *stuff* in it.

### Your own machine

Various Pythons may or may not work for this – I use 3.10 or 3.11, not exactly sure about more recent ones. I think all of the `pip install` commands are in the Jupyter notebooks themselves, so you shouldn't need anything on that front. Maybe `brew install ffmpeg`, depending on what you're up to.



## 2025-beginner-foia.md

Beginner track: How to request data and documents: FOI
Tisha Thompson, ESPN
Andrew Pantazi, independent journalist
Kate Martin, APM Reports

Today you will learn
How to negotiate with officials
Appeal methods and mindset
Minimum and maximum story
Best way to ask for text messages and emails
Talk about this from a mentor/editor’s perspective
Strategies for data requests
Ways to organize your FOIAs and deadline reminders

ALWAYS TRY TO GET IT WITHOUT FOIA FIRST 


THINK ABOUT HOW MANY RECORDS YOU MAY RECEIVE
“SNOW” and “ICE” = roughly 4,000 emails from one agency in a 24 HR period 

Keyword search for “SEAT” = “Seatgeek”, “Superseats USA” & “Supreme Seats”

But “SEAT” is also part of the word “Seattle”
In Washington state, there 6,000+ businesses containing the word “Seattle” 


YOU HAVE TO PROVE WHY IT SHOULD BE “EXPEDITED”
I request expedited processing of this request because it is for documents relating to a public controversy over the use of conservation land known as "Greenbury Point" that is under the control of the Department of the Navy. It is urgent to inform the public about the actual or alleged federal government activity with this land as it will have significant impact on residents who live near and around the property, as well as those connected to the U.S. Naval Academy, and has been the topic of public meetings and news coverage, a list of which includes, but is not limited to stories I am submitting as an attachment to this FOIA request. 

“BONA FIDE” WITH EXPLANATION
I am requesting a fee waiver as I am a bona fide member of the media collecting this information as part of the newsgathering process and not for commercial use. The documents requested are of great concern to the public and our readers as they relate to the use and operation of land owned by the Navy and the disclosures are likely to contribute significantly to a better understanding of the government’s decision making in relation to the use of that land, which is mostly unknown despite significant news coverage of the topic.
If you determine, however, that fees must be assessed, I am willing to pay up to $300. If the cost should be more than that, please provide an estimate of fees. 


YOU NEED TO RESEARCH THE LAW BEFORE YOU SEND!

WHAT I DO EVERY SINGLE TIME BEFORE I SEND A REQUEST


I google “Reporters Committee Open Government” for state requests
and “Reporters Committee FOIA” for federal requests

So let’s do that right now…


Which brings us to appealing a records denial
https://drive.google.com/file/d/1iwGOnivhB3Y7OhwvkUh1Iy-msBaPck24/view?usp=sharing 


https://www.rcfp.org/wp-content/uploads/imported/FOIAapp-samples-March72011.pdf 


The HARDEST FOIA LESSON I’ve ever learned arrived in this letter…

I spent 5+ years fighting for this document from the State Department…

Only to have the local police departments then deny my speeding ticket FOIAs…

So I went to every courthouse in the DC region and pulled them manually…

And had to wait again because many were in the “archives”…

After I got the tickets (hundreds of tickets)…

I made myself a database…

Did some SQL queries (yeah baby, you heard that right, SQL)…

And found me some diplomats (and often the children of diplomats) …

AFTER 6+ YEARS 
& 2 JOBS 
IRE FOIA Award Finalist

BUT ALL MY INFO WAS SIX YEARS OLD!

The hardest lesson I ever learned when the ambassadors denied my appeal for current records…
I WILL NEVER AGAIN WRITE
“From January 1, 2003 until the present day.”
I NOW WRITE
“From January 1, 2003 until 
this request is processed.”

What Your Editor Needs to Know (And How They Can Help You)
Your editor isn’t just a gatekeeper—they’re your ally.
The better you communicate, the more support (and resources) you’ll get.
Avoid frustration: Know what your editor needs before they ask.
Don’t let records delays stall your reporting or writing. Let your editor help you map out what story you can do with or without the records.
Share your system for tracking public records (a spreadsheet or some other database) with your editor with key information.

Essential - Does this align with our mission?
Distinct - Are we uniquely positioned to tell this story?
Impact - Could this lead to meaningful change? Can the problems described be rectified?
Timing - Is this the right moment for the story?
Obstacles - Are there legal, ethical, or reputational risks? What are the biggest hurdles in getting this story done?
Result - What’s the biggest vs. minimum viable version of the story? When will we know it’s time to walk away?
EDITOR CHECK:

WHAT YOUR EDITOR WANTS TO KNOW

B.E.S.T. – How Your Editor Can Back You Up
B – Boss Voice – Editors can call FOIA officers and demand answers.
E – Escalation – They can push agencies, PIOs, or officials when you're being ignored.
S – Strategic Planning – They can help figure out workarounds if records are denied.
T – Taking Legal Action – They can help persuade your org to sue when necessary.
If you're stuck, ask: "Can my editor step in and push for this?"

Request Broad Data to Narrow In
Ask for metadata or summary-level data that doesn’t require redaction.
Provide technical instructions—agencies often claim they “can’t extract” data when they can.
Use legal precedent to assert your right to electronic records.
Example: Instead of requesting full emails (which the agency said would take years to redact), I asked for email metadata. I provided case law for why they would need to give these records, AND I even gave them the PowerShell commands for extracting the metadata.
What to do if you don’t know what data the agency has

What to do if you don’t know what data the agency has
Request System Manuals to Reveal Hidden Data
Agencies may claim they “don’t have” data simply because they don’t know where it’s stored.
Request system documentation to uncover what data fields exist and how they’re recorded.
Example: Understanding a Crime Incident Database
"I am requesting any contracts, instruction manuals, data dictionaries, glossaries of terms, record layouts or handbooks related to the Sheriff’s Office’s crime incident database or case management system."
🔹 Why this works:
✅ Exposes what data is actually collected.
✅ Helps refine follow-up requests.
✅ Prevents agencies from denying data exists.

Sample records request form letter
Link: https://bit.ly/records-template
Includes tips for:
Email requests
Data requests
Text/instant messages


Track your requests with notiFOIA
How tracking your request and getting email notifications about them can help you succeed and save you time

Kate Martin, correspondent, APM Reports

What is notiFOIA?
bit.ly/notiFOIA
It’s a Google sheet that tracks your records requests and sends you an email reminder when you haven’t heard from an agency.
It can be a repository for your records so you can find them quickly
It’s great if you…
File multiple records requests per week
Are worried a request will get lost in the shuffle
Want notifications without using a third-party service
Collaborate: Multiple people can be notified of overdue requests

A tour of notiFOIA: tabs
bit.ly/notiFOIA
How to: Instructions for installation
Main: Where you put your records request information
State_info: Info about each state’s records laws, with links to example FOIA letters and the RCFP page for each and includes calculations for when records are due (more on this later)
Dictionary: What each field means


A tour of notiFOIA: Main interface

A tour of notiFOIA: Main interface

A tour of notiFOIA: Main interface

A tour of notiFOIA: Main interface
bit.ly/notiFOIA
Marking anything under “records received” stops the clock and means you will no longer get reminder emails
If an agency asks for an extension, you can extend the deadline by typing a number into the “add days” column

A tour of notiFOIA: State info tab
In some states, agencies must respond by a certain number of days. Others have no limit or the agency must respond “promptly,” whatever that means.
For states that don’t set a specific timeframe, default to respond is 10 days.

A tour of notiFOIA: emails
bit.ly/notiFOIA
You get one email per line in the spreadsheet
I use filters to send these to a folder and try to process them once a week or when I have spare time

A tour of notiFOIA: emails
bit.ly/notiFOIA
uniqueID refers to the ID in the spreadsheet
Includes notes I wrote checking up on request progress
Includes contact info of records officer

notiFOIA: Setup
bit.ly/notiFOIA
Check HOW TO tab for instructions
Step 1: Click “file” then “Make a copy”
Step 2: Activate the app script as-is (see instructions in “How to” tab)
There should be no need to update the app script
Step 3: Decide how often do you want alerts? (I pick Tuesday mornings)
Step 4: Happy FOIAing!

Helpful resources
The Reporters Committee for Freedom of the Press: www.rcfp.org. Includes state-by-state guides
The National Freedom of Information Coalition – www.nfoic.org
Student Press Law Center: https://splc.org/
Records request form letter: bit.ly/records-template
Track your records requests and receive email reminders from a Google Sheet with notiFOIA: bit.ly/notiFOIA
FOIA Wiki: https://foia.wiki/

bit.ly/beginner-foia
Questions?

Beginner track: How to request data and documents: FOI
Tisha Thompson, ESPN
Andrew Pantazi, independent journalist
Kate Martin, APM Reports


## Pre-requisites

You will need:

- A **GitHub account** for GitHub Actions and GitHub Codespaces.
- A **Python environment** - I recommend GitHub Codespaces for this, but you can run things on your own laptop if you like.
- A **Google account** for access to [Google AI Studio](https://aistudio.google.com/). You may find that your work Google account is unable to access that tool, in which case you can try a personal account instead.



## Structure of this session

This is an interactive, hands-on workshop. We'll be working through four exercises:

1. Building a [Git scraper](https://simonwillison.net/2020/Oct/9/git-scraping/) - an automated scraper in GitHub Actions that records changes to a resource over time
2. Using in-browser JavaScript and then [shot-scraper](https://shot-scraper.datasette.io/) to extract useful information
3. Using [LLM](https://llm.datasette.io/) with both OpenAI and Google Gemini to extract structured data from unstructured websites
4. [Video scraping](https://simonwillison.net/2024/Oct/17/video-scraping/) using [Google AI Studio](https://aistudio.google.com/)


## 1. Git scraping

A **git scraper** is a GitHub repository configured to use GitHub Actions to scrape websites or other online resources and record changes to them over time.

Here are [437 examples](https://github.com/topics/git-scraping?o=desc&s=updated) of this category of repo, ordered by most recently scraped! I have a whole lot more notes about [git-scraping on my blog](https://simonwillison.net/tags/git-scraping/).

To create a basic one, first sign into GitHub and then visit this repository:

https://github.com/simonw/git-scraper-template

This is a **template repository** - you can select "Use this template" and then "Create a new repository" to start your own based on the template.

Enter the URL of the website - or direct URL to a JSON file - in the **description** field when you create the repository. It will be configured to track changes to that page once per day, or any time you manually activate the scraper.

Try with this from https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

    https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson

To avoid wasted resources, you should deactivate your scraper at the end of this workshop. You can do that by adding a `#` in front of this line in your `.github/workflows/scrape.yml` file:

    - cron: '23 6 * * *'


**Bonus**: if you want notifications every time something changes, every GitHub repository includes a hidden RSS feed. Add `.atom` to the commits page URL, for example:

    https://github.com/simonw/scrape-openai-models/commits/main.atom

I subscribe to these in [NetNewsWire](https://netnewswire.com).



## 2. Scraping with in-browser JavaScript

Websites are complicated beasts these days. Scraping just through parsing HTML often doesn't work - we need to load up the entire website in a real browser first.

Some websites are resistant to scraping techniques. We're journalists, we have legitimate reasons to need that data!

Using **JavaScript** can solve both of these problems. We can extract any data that's visible on the page, and we can bypass all known forms of anti-scraping technology if we start by doing it in our own browsers.

Here's a version of a function I use all the time:

```javascript
function tableToObjects(table) {
  const rows = Array.from(table.querySelectorAll("tr"));
  if (rows.length === 0) {
    return [];
  }
  const headers = Array.from(rows[0].querySelectorAll("th"))
    .map(headerCell => headerCell.textContent.trim());
  if (headers.length === 0) {
    return [];
  }
  const result = [];
  for (let i = 1; i < rows.length; i++) {
    const row = rows[i];
    const cells = Array.from(row.querySelectorAll("td"));
    if (cells.length === 0) {
      continue;
    }
    const rowObject = {};
    headers.forEach((header, index) => {
      if (index < cells.length) {
        rowObject[header] = cells[index].textContent.trim();
      }
    });
    result.push(rowObject);
  }
  return result;
}
```
Navigate to https://doge.gov/spend and open the browser DevTools and paste that it.

Now run this:
```javascript
copy(tableToObjects(document.querySelectorAll("table")[0]))
```
Paste the result into a text editor. You should get JSON data extracted from the table.

### Using this for infinite scrolling web pages

I wrote about this trick in [Collecting replies to tweets using JavaScript](https://til.simonwillison.net/twitter/collecting-replies). I'll demonstrate the pattern, and if you have a Twitter account you can try it yourself.

Visit a tweet with a lot of replies, then run the following in your browser DevTools:

```javascript
window.tweets = window.tweets || [];
let seenHrefs = new Set();

function extractNumber(el, selector) {
  const element = el.querySelector(selector);
  if (element && element.getAttribute) {
    const match = element.getAttribute("aria-label").match(/(\d+)/);
    return match ? parseInt(match[0], 10) : 0;
  }
  return 0;
}

function collectTweets() {
  // Ditch any … elements
  document.querySelectorAll("span").forEach((span) => span.textContent.trim() === "…" && span.remove());
  Array.from(document.querySelectorAll("[data-testid=tweet]"), (el) => {
    const datetime = el.querySelector("time")?.dateTime || "";
    const username = el.querySelector('[data-testid="User-Name"] a')?.href.split("/").slice(-1)[0] || "";
    const tweet = el.querySelector('[data-testid="tweetText"]')?.innerText || "";
    const href = el.querySelector("time")?.closest("a")?.href || "";
    const likes = extractNumber(el, '[data-testid="like"]');
    const impressions = extractNumber(el, '[aria-label*="View post analytics"]');
    const retweets = extractNumber(el, '[aria-label*="Repost"]');
    return { datetime, username, tweet, href, likes, impressions, retweets };
  }).forEach((tweetObj) => {
    // Filter out tweets with previously seen hrefs and add new ones to window.tweets
    if (!seenHrefs.has(tweetObj.href)) {
      seenHrefs.add(tweetObj.href);
      window.tweets.push(tweetObj);
    }
  });
}

setInterval(collectTweets, 500);
```

Scroll down until you have viewed all of the replies, then run this:
```javascript
copy(tweets);
```
Paste into a text editor to see the data you have collected.

### Automating one of these with shot-scraper

If you're going to use GitHub Codespaces for this, click "Use this template" and then "Open in codespace" on this repository. Wait for that to boot up and you should have a terminal where you can start running these commands.

First, install `shot-scraper`:

```bash
pip install shot-scraper
shot-scraper install
```
You can use **shot-scraper** to capture entire screenshots of web pages, which can be useful for archiving projects:

```bash
shot-scraper https://doge.gov/
```
This will produce a VERY long PNG image. You can get a shorter one (and use JPEG instead, which is smaller) like this:
```bash
shot-scraper https://doge.gov/ -o doge.jpg -h 1024
```
The [shot-scraper javascript](https://shot-scraper.datasette.io/en/stable/javascript.html) command is more interesting. It can execute JavaScript against the page and return the results. Here's a simple example:
```bash
shot-scraper javascript doge.gov document.title
```

> `"Work | DOGE: Department of Government Efficiency"`

A more complex one ([thanks, Claude](https://claude.ai/share/58b8c5da-1514-426d-a836-a1d538f3a048)) to return their "estimated savings":
```bash
shot-scraper javascript doge.gov/savings "Array.from(
  document.querySelectorAll('p')
).find(
  p => p.innerText.includes('Estimated Savings')
).nextElementSibling.innerText;"
```
I got:
> `"$105B"`

You can add `-r` (for `--raw`) to get back that string without it being wrapped in quotes.

Now let's use our example from earlier:

```bash
shot-scraper javascript doge.gov/spend '
() => {
  function tableToObjects(table) {
    const rows = Array.from(table.querySelectorAll("tr"));
    if (rows.length === 0) {
      return [];
    }
    const headers = Array.from(rows[0].querySelectorAll("th"))
      .map(headerCell => headerCell.textContent.trim());
    if (headers.length === 0) {
      return [];
    }
    const result = [];
    for (let i = 1; i < rows.length; i++) {
      const row = rows[i];
      const cells = Array.from(row.querySelectorAll("td"));
      if (cells.length === 0) {
        continue;
      }
      const rowObject = {};
      headers.forEach((header, index) => {
        if (index < cells.length) {
          rowObject[header] = cells[index].textContent.trim();
        }
      });
      result.push(rowObject);
    }
    return result;
  }
  return tableToObjects(document.querySelectorAll("table")[0]);
}
'
```
Here's [the JSON I got from that](https://gist.github.com/simonw/734d683dd64f4ba535007a9e925eea51).

You can combine `shot-scraper javascript` with Git scraping. I do that in my [simonw/scrape-hacker-news-by-domain](https://github.com/simonw/scrape-hacker-news-by-domain) repository, which I wrote about in detail in [Scraping web pages from the command line with shot-scraper](https://simonwillison.net/2022/Mar/14/scraping-web-pages-shot-scraper/).

I also wrote up a trick for working around scraping prevention services that exclude GitHub Actions by proxying traffic through an Apple TV on a home network, see [Using a Tailscale exit node with GitHub Actions](https://til.simonwillison.net/tailscale/tailscale-github-actions).


## 3. Structured data extraction using LLM

Here's [documentation on schemas in LLM](https://llm.datasette.io/en/stable/schemas.html).

You'll need API keys for this. Visit [this page](https://tools.simonwillison.net/encrypt#6s444Mi4bEHi9dkcaWxk3ux3EplN9jZyqGpT8MaBcRu7A0FjyxSaAHEyxH4CsMcY25d8qpB2u2XZ687VA41OgfjIdD5HXYKxiTrlJZbdkVM7JiObFnijGFtkYbJMscV4i7qKyLAcO9eHvfe9m+G6fQatlPYLQxPsKqo6GPe+pLHGWx2TZGtZVMtZtr1onaVf2ji3rfRj2yICkGhobv5WXM2rv3Eqr4T163AJ1nv4L3NdGHR6wiI4G+hbtmKvbWimTq5wtns4Cjs9dT1NzchZdLG0UKpGjGqJMUZ4LVcdhNuPSMx3SNWOa7ALd83nv04DUpMPZRYcYRnhQ4d1OphEHiLeqzgsBPuFbZco1TR+kalaqOI05hJh) and enter the passphrase distributed during the workshop to get OpenAI and Gemini keys that you can use during the workshop.

After the workshop you'll need your own. You can get [OpenAI keys here]() (you'll likely have to setup billing, but the cost is extremely low) and [Google Gemini keys here](https://aistudio.google.com/apikey) (they have a generous free tier and extremely inexpensive prices beyond that).

Start in Codespaces (or your local Python environment). Run this:

```bash
pip install llm
llm keys set openai
# Paste your OpenAI key here

llm 'five neat facts about pelicans'
```
Now let's try a schema. Let's invent some dogs:
```bash
llm 'invent some cool dogs' --schema-multi 'name,age int,bio'
```
If you have `jq` installed you can pretty-print the most recent logged data like this:
```bash
llm logs --data -c | jq
```
Where schemas get _useful_ is when we used them to extract data from unstructured pages.

Let's try a version of that now:
```bash
curl 'https://www.whitehouse.gov/presidential-actions/' | \
  llm --schema-multi 'title,url,date:yyyy-mm-dd' 'extract executive actions'
```
Web pages can get large with a lot of tokens. Let's check how many we used:
```bash
llm logs --short --usage
```
I got back this:
```
- model: gpt-4o-mini
  datetime: '2025-03-08T16:05:05'
  conversation: 01jnv81yhk4e0npgjksrh555j6
  prompt: <!DOCTYPE html> <html lang="en-US"> <head> <meta charset="UTF-8" /> <meta
    name="viewport" content="width=device-width...
  usage:
    input: 60822
    output: 647
```
Using [this pricing calculator](https://tools.simonwillison.net/llm-prices) we can see that for GPT-4o mini with 60,822 input tokens and 647 output tokens the cost is 0.9511 cents.

That's one of the cheapest models though, this could cost a _lot_ more with some of the others. GPT-4.5 would charge $4.65 for the same thing!

You can estimate the number of tokens before attempting a prompt using [ttok](https://github.com/simonw/ttok):
```bash
pip install ttok
curl 'https://www.whitehouse.gov/presidential-actions/' | ttok
```
Let's try the same thing again using Google's cheaper models, Gemini 2.0 Flash:
```bash
llm install llm-gemini
llm keys set gemini
# Paste key here

curl 'https://www.whitehouse.gov/presidential-actions/' | \
  llm --schema-multi 'title,url,date:yyyy-mm-dd' 'extract executive actions' -m gemini-2.0-flash
```
That cost just 0.6341 cents!

I tried it against their even cheaper model, `gemini-1.5-flash-8b-latest`, but that one failed to return any results. It's good practice to try different models and figure out the cheapest one that works for your particular problem.

For this particular website the `shot-scraper` technique shown earlier is a better bet - it's much more reliable than LLMs.

Where LLM scraping gets _really_ interesting is on harder content, such as PDFs.

The **FEMA Daily Operations Briefing** is an _incredible_ document, sent out by email to subscribers once a day.

[data-liberation-project/fema-daily-ops-email-to-rss](https://github.com/data-liberation-project/fema-daily-ops-email-to-rss) is an excellent project that tracks those daily releases so you don't have to subscribe to their list.

The PDF briefing for March 8th 2025 [can be found here](https://content.govdelivery.com/attachments/USDHSFEMA/2025/03/08/file_attachments/3187534/FEMA%20Daily%20Ops%20Briefing%2003-08-2025.pdf) (here's [a backup copy](https://static.simonwillison.net/static/2025/FEMA%20Daily%20Ops%20Briefing%2003-08-2025.pdf)).

Page 10 is a good target for extracting structured data:


We'll feed the whole PDF file to Gemini 2.0 Pro (Experimental) with a schema:

```bash
llm 'extract declaration requests' \
  -a 'https://content.govdelivery.com/attachments/USDHSFEMA/2025/03/08/file_attachments/3187534/FEMA%20Daily%20Ops%20Briefing%2003-08-2025.pdf' \
  --schema-multi 'state_tribe_territory,incident_description,type,IA bool,PA bool,HM bool,Requested:YYYY-MM-DD guess year based on it being March 2025 now' \
  -m gemini-2.0-pro-exp-02-05
```
Here's what I got:
```json
 {"items": [
    {
      "HM": false,
      "IA": true,
      "PA": true,
      "Requested": "2024-07-20",
      "incident_description": "Severe Storms, Tornadoes, Straight-line Winds, and Flooding",
      "state_tribe_territory": "NY",
      "type": "EM"
    },
    {
      "HM": true,
      "IA": true,
      "PA": true,
      "Requested": "2024-12-02",
      "incident_description": "Park and Borel Fires (Appeal)",
      "state_tribe_territory": "CA",
      "type": "DR"
    },
    {
      "HM": true,
      "IA": true,
      "PA": true,
      "Requested": "2024-12-20",
      "incident_description": "Severe Storms, Straight-line Winds, Tornadoes, and Flooding",
      "state_tribe_territory": "OK",
      "type": "DR"
    },
    {
      "HM": true,
      "IA": false,
      "PA": true,
      "Requested": "2025-01-14",
      "incident_description": "Severe Storms, Straight-line Winds, Flooding, Landslides, and Mudslides",
      "state_tribe_territory": "WA",
      "type": "DR"
    },
    {
      "HM": true,
      "IA": true,
      "PA": true,
      "Requested": "2025-01-30",
      "incident_description": "Severe Winter Storms and Snowstorms",
      "state_tribe_territory": "KY",
      "type": "DR"
    },
    {
      "HM": true,
      "IA": true,
      "PA": true,
      "Requested": "2025-02-26",
      "incident_description": "Severe Winter Storms, Tornadoes, and Flooding",
      "state_tribe_territory": "VA",
      "type": "DR"
    }
  ]
}
```

This Gemini 2.0 Pro model is currently free, but has strict rate limits. Try some of the other models to see how well they do - `gemini-2.0-flash` and `gemini-2.0-flash-lite` for example.

OpenAI model can't yet handle PDFs but they work very well with images. You can run that screenshot I saved of the PDF through GPT-4o mini like this:

```bash
llm 'extract declaration requests' \
  -a 'https://raw.githubusercontent.com/simonw/nicar-2025-scraping/refs/heads/main/fema-page-10.png' \
  --schema-multi 'state_tribe_territory,incident_description,type,IA bool,PA bool,HM bool,Requested:YYYY-MM-DD guess year based on it being March 2025 now' \
  -m gpt-4o-mini
```
You can use the filepath directly rather than a URL, if you have the file saved locally.

For a really fun challenge, see if you can get useful structured data out of the extremely complicated map on page 8!




## 4. Video scraping using Google AI Studio

Let's finish with a new technique that I think is really promising: **video scraping**.

This is the ultimate hack for scraping data from a website that really, really doesn't want to be scraped.

The Gemini models can accept video as input. The trick is simple: record a video of your screen, browse through a website clicking on different links and pausing for a few seconds each time, then get Gemini to turn that video into JSON data.

You can do this using LLM, but in this case let's explore Google's AI Studio tool instead - which is _free_ for almost everything interesting you may want to do with it.

(Does it train on your input data if you're using it for free? Maybe - I don't have a solid answer about that yet. So don't try it out with anything confidential.)

https://aistudio.google.com/

The SEC website is notoriously resistant to scraping tools. Let's try and pull some useful data out of this document:

https://www.sec.gov/ix?doc=/Archives/edgar/data/1444822/000119312524201935/d882430d485bpos.htm

1. Scroll to an interesting section of the document.
2. Load "QuickTime Player" (I'm afraid I don't know what the equivalent tool on Windows or Linux is) and use "File -> New Screen Recording".
3. Scroll through the relevant sections, pausing for a second or two on each individually interesting screen
4. Upload the resulting video to AI Studio and start prompting!
5. Optionally, try using their schema extraction tool illustrated here:


It's also worth trying out the AI Studio "Stream Realtime" option, though I've not figured out how to use that for scraping projects yet.


## I want to talk to you about applying these techniques in your newsroom

We are building out a suite of tools to help implement these patterns, and I'd love to learn what you need from them and how we can collaborate in the future.

Email me at `swillison@` Google's email provider, or come and grab me in the corridor during the conference.



## Further tools and resources

- [git-scraper-template](https://github.com/simonw/git-scraper-template) is a tool for quickly getting started with [Git scraping](https://simonwillison.net/2020/Oct/9/git-scraping/) - see [my blog](https://simonwillison.net/2025/Feb/26/git-scraper-template/) for details.
- [shot-scraper-template](https://github.com/simonw/shot-scraper-template) is a similar tool, described in [Instantly create a GitHub repository to take screenshots of a web page](https://simonwillison.net/2022/Mar/14/shot-scraper-template/). 
- [shot-scraper har](https://shot-scraper.datasette.io/en/stable/har.html) is a new command I built for generating an HTML Archive file of a page. Use the `--zip` option to get that as a zip file, which can include JSON and other assets used to assemble the page.
- [git-history](https://github.com/simonw/git-history) is a tool for turning GitHub commit logs into a SQLite database you can query using [Datasette](https://datasette.io/). 


## Installation

Run these commands (ideally in a virtual environment created using your preferred mechanism):

```bash
pip install -r requirements.txt
shot-scraper install
```

I create my virtual environments like this:

```bash
python -m venv venv
source venv/bin/activate
```



## 2025-data-reporting-smaller-teams.md

Data reporting for smaller teams
bit.ly/small-data-j
Kate Martin, APM Reports
Cody Lillich, Arizona's Family (KTVK/KPHO-TV)
Junyao Yang, Mission Local
Justin Myers, Chicago Sun-Times

Cody Lillich
Senior Investigative Producer
KTVK 3TV/KPHO CBS 5 (Phoenix)
Email: cody.lillich@graymedia.com 
X: @CodyLillich | Bluesky | LinkedIn


Data Reporting in Television
“Data Team” may only be you
What can you get – and get quick?
Think about what you might need in a moment’s notice
City salaries, including OT and “other pay”
Vehicle crash data
Assessor data
Be a resource
You’ll quickly be the go-to for all things data (that may and may not exist)
Hold mini-sessions with staff to spread the knowledge (and so it’s not all on you!)
One Sheets on topics that are guaranteed to come up:
Crime
Wildfires
Extreme Heat

State Crash Data
Most states require a form to be filled out for every crash.
State DOTs typically compile all of this info into a database.
This information is a goldmine.
In Arizona we get data on:
# deaths, # injuries
Pedestrian-involved?
Seatbelt use
Violation(s)
Distracted?

This is what the state puts out…
Lengthy PDF
Good for quick data
But you want what feeds this!

State Crash Data

Assessor Data
Assessor Data can tell lots of 
information:
Average price
Rental Indicators
People who own multiple 
Properties
Investors buying thousands of Phoenix-area homes as rent prices spike

Immigration Data
Problem: CBP data portal only goes back to FY2022.

Immigration Data
Problem: CBP data portal only goes back to FY2022.
Solution: Scrub monthly pdfs to get archival data to give a more accurate timeline along our sectors.
Provides our producers with quick data and perspective that is updated once a month.

Junyao Yang
Data reporter, Mission Local
Email: junyao@missionlocal.com
Bluesky: @junyao-yang.bsky.social
Instagram: @junyaophotos

Data reporting in a small newsroom
Mission Local: 7 reporters, 3 editors
3 data reporters — but we are also beat reporters

The work
Simple graphics for quick turnaround stories
Datawrapper
Who were the most successful endorsers? Mayor Breed, her allies — and Republicans.

The work
Simple graphics for quick turnaround stories
Datawrapper
Flourish → SVG → Illustrator
QGIS → SVG → Illustrator
SF Police Commission critics fail to understand how it works, promoting misinformation

The work
Simple graphics for quick turnaround stories
Datawrapper
Flourish → SVG → Illustrator
QGIS → SVG → Illustrator
Enterprise stories
Mapbox
Javascript

The work
Simple graphics for quick turnaround stories
Datawrapper
Flourish → SVG → Illustrator
QGIS → SVG → Illustrator
Enterprise stories
Mapbox
Javascript
Python

The work
Design
Making sure things look pretty
Training for colleagues: walk through easy-to-use tools
Datawrapper and OpenRefine or even Google Sheets are a good start

Lessons
Check your work
Always ask sources for datasets!
Befriend the data stewards in your city
Design consistency
Communicate often, show drafts — Save yourself from unnecessary revisions
Keep the data team (no matter how small) organized


Email: kmartin@apmreports.org
Bluesky/Twitter: @katereports
Kate Martin
Correspondent, APM Reports

Data reporting at small newspapers
I was the only data reporter in my newsroom for most of my career.
Started with Excel, moved to SQL, then R and dabble in Python
Constantly pushed myself to learn new skills.
Evangelized to colleagues about data reporting.
Learned strategies to get editor buy in.
Workplaces: Loveland Reporter Herald, Skagit Valley Herald, The News Tribune, Carolina Public Press, NBC News, APM Reports

Anyone can become a data reporter
I had no idea how to use Excel.

Yes, I added these up by hand. With a pen.

So, I learned!


When you get data
Make a copy
Create two folders: Original and working
You want to keep your original data pristine in case you mess up
Name files and versions in a reasonable way:
Schools.final = not good 
Schools.1.0 = better
Schools.2013-02-03 = best
Find a system that works for YOU!

Think of data as a source
You wouldn't run a one-source story on most things. Don't depend on data for the single source either.
Data can: 
answer questions, raise questions, mislead you, and point you in the wrong direction
You can: 
misinterpret data, take it out of context, write an incorrect formula
find hidden gems, fact-check source statements, bring hidden issues to light


Time management in small newsrooms
There is never enough time.
Keep two running lists of story ideas:
One list of stories you can do today to satisfy your boss
One list of project candidates that you can chip away at
Have five minutes? File records requests, look for documents and experts, write sections of the story
Write a story and don’t turn it in. Work on your project story. When your boss asks for your daily story, then turn it in.

Check yourself before you wreck yourself
That story you thought was awesome, might not be
WARNING SIGN: If you are really excited about a story, double check your facts and formulas. You might have made a BIG error.
Report it out a little before you tell your boss
When you know the story is solid, send your boss a memo with a few paragraphs
Underpromise and overdeliver
Have a minimum viable product if the story falls through
This is all about managing expectations

You can do linear regressions!!
Helps predict how poverty affects test scores.

Other examples:
Pollution and asthma
Stress levels and exercise
Height and weight

Beware of spurious correlations


Source: https://www.tylervigen.com/spurious-correlations

Email: 		justin@justinmyers.net
Bluesky: 		@justinmyers.net
Fediverse: 	@myersjustinc
					@mastodon.sdf.org
Justin Myers
Interactives editor, Chicago Sun-Times
(any pronouns)


Experience with teams of all sizes
Solo with occasional design help
About 4 to 8, with different specialties
15 or so, and managed about 10

And now:
A newsroom in transition
Am I all alone?
Am I on a four-person team?

And now:
A newsroom in transition
Chicago Public Media—produces both the Sun-Times and WBEZ
Buyouts, reorganization
Am I all alone?
Am I on a four-person team?

And now:
A newsroom in transition
Chicago Public Media—produces both the Sun-Times and WBEZ
Buyouts, reorganization
Am I all alone?
Sun-Times has one dedicated person for graphics/data/etc.
Am I on a four-person team?

And now:
A newsroom in transition
Chicago Public Media—produces both the Sun-Times and WBEZ
Buyouts, reorganization
Am I all alone?
Sun-Times has one dedicated person for graphics/data/etc.
Am I on a four-person team?
WBEZ has three dedicated people focusing more on data reporting
Had been up to seven over the summer

Actual graphics
Help others with heavy lifting
Occasional technical R&D
“Graphics”

Actual graphics
Daily for print and online
Big feature presentations
Stuff in between
Help others with heavy lifting
Occasional technical R&D
“Graphics”

Actual graphics
Daily for print and online
Big feature presentations
Stuff in between
Help others with heavy lifting
Occasional technical R&D
“Graphics”

Actual graphics
Daily for print and online
Big feature presentations
Stuff in between
Help others with heavy lifting
Mostly investigative teams
Occasional technical R&D
“Graphics”

Actual graphics
Daily for print and online
Big feature presentations
Stuff in between
Help others with heavy lifting
Mostly investigative teams
Occasional technical R&D
Workflows, tools, etc.
“Graphics”

Two guiding principles
Enable as much reuse as possible, within reason
Remember later WTF I’ve done

Python, in JupyterLab notebooks
Lots of GIS-related work
Tools and techniques

Python, in JupyterLab notebooks
DVC for backing up large files outside of GitHub
(But use whatever works in your specific context, seriously!)
Lots of GIS-related work
Tools and techniques

Python, in JupyterLab notebooks
DVC for backing up large files outside of GitHub
(But use whatever works in your specific context, seriously!)
Lots of GIS-related work
QGIS for experimenting
GeoPandas for posterity
Illustrator for publication
Tools and techniques

Know how to share intermediate results with people
How do you provide your colleagues with…
Communicate, communicate, communicate

Know how to share intermediate results with people
Even simple annotated screenshots help a ton
How do you provide your colleagues with…
Communicate, communicate, communicate

Know how to share intermediate results with people
Even simple annotated screenshots help a ton
How do you provide your colleagues with:
Clarity?
Empowerment?
Inspiration?
Communicate, communicate, communicate

Free/cheap resources (including from IRE)
https://www.ire.org/join-ire/member-benefits/
Thousands of tipsheets (useful for exploring new topics)
Curated databases (free and paid): dams, disaster loans, business loans
Tableau Public and Tableau Prep Builder: Free license
SmartProcure/GovSpend: Discounted subscription for IRE members
PacerMonitor: Discounted subscription for IRE members

Questions?
bit.ly/small-data-j

Data reporting for smaller teams
Kate Martin, APM Reports
Cody Lillich, Arizona's Family (KTVK/KPHO-TV)
Justin Myers, Chicago Sun-Times
Junyao Yang, Mission Local


## 2025-extracting-data-documents-ai.md

Extracting data from documents with AI
Rosmery Izaguirre
Sean McMinn
Jonathan Soma
tinyurl.com/mr2petff

What we’ll cover 
What to do when you have a standardized document format
What to do when you have several different kinds of document formats
What to do when you need more flexible document workflows
Rosmery Izaguirre
Data reporter, POLITICO
Sean McMinn
Data editor, POLITICO
Jonathan Soma
Professor, Columbia University

Transforming PDF text into data with Google Pinpoint

Pinpoint features
Create a searchable repository of PDFs
Automatically parses the documents and attempts to organize content
Keeps documents private. Shareable through Google collab features
Extract structured data
Uses AI and machine learning
Works best with a collection of documents that follow a similar format. Uses an annotated template to “learn”

California Lawmaker Gift Forms 

Extract structured data using Pinpoint AI and machine learning 
Paolo Pinpoint
The princess in question:

Golden Document
One “master” document to act as a template for the rest fo the collection
How to choose your golden doc?
Ideally the golden doc will be one with as many fields filled in order to let Pinpoint know what it should expect

Key/Value pair recognition
Text sections - Key is the field name (eventually turns into column name) and the value is the filled in portion
Checkbox - boolean T/F based on if checkbox is filled in

Repeated Sections (purple)
Limitation identified through Pinpoint support:
Repeated sections are not supported horizontally, meaning that each box with gift fields could not be its own section instead two boxes were treated as one section that repeated down 

Advanced Pinpoint
If there is slight variance between documents, multiple golden documents can be annotated to address this.
Designating missing/deleted fields between golden documents
Highly recommend reaching out to pinpoint support during testing and annotating
pinpoint-support@google.com

Results
We’re given a pretty decent extraction, but further cleaning is needed.

How can we check and clean the results Pinpoint provided?
Spot check
Programmatically count a repeating field and make sure it lines up
Put it through a different type of parser using OpenAI or other programmatical methods

Other extraction tools that have a GUI/are beginner friendly
Adobe Acrobat Pro
Tabula
PyPDF2
Docparser (paid)
Nanonets (paid)

Adams County, Pa.
White Pine County, Nev.
Beaver County, Pa.
It’s just votes, how many ways can you really publish them?

What it mean to work with a schema in GPT 

What it mean to work with a schema in GPT 
What if we could guarantee….
Location (str) 
AWARD ID (str)
CONTRACT_PIID (str)
USAID Bureau or Country (str)
CONTRACT_DESCRIPTION (str)
Estimated_cost(int) 
Obligated_to_date (int)

We want a prompt and schema that will handle any of those.
Extract data into the following format. 
If there are zero votes, do not include it. Do not include write-in candidates. For president, only include votes for Donald Trump or Kamala Harris.
Just FYI, precinctName often has an id number either before or after it, often formatted like "0101". You should capture that as part of precinctName. If there is no precinctName on the page, please put "Unknown". The precinctName will sometimes have a precinct or ward number, please capture that, but in those cases it often has an accompanying city or neighborhood name, so make sure you capture that as well.  
Note that we are not looking for only election day or mail in votes, but we want total votes per precinct. 

{  "name": "election_result",
  "strict": false,
  "schema": {
    "type": "object",
    "properties": {
      "results": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "candidateName": {
              "type": "string",
              "description": "The name of the candidate",
              "enum": [
                "Harris",
                "Trump"
              ]
            },
            "precinctName": {
              "type": "string",
              "description": "The name of the precinct where the race is being held, usually found somewhere on the page, can be shared between races."
            },
            "totalVotes": {
              "type": "integer",
              "description": "The total number of votes the candidate received"
            }
          },
          "required": [
            "candidateName",
            "precinctName",
            "totalVotes",
            "officeName"
          ],
          "additionalProperties": false}}},
    "required": []}}


We want a prompt and schema that will handle any of those.
Extract data into the following format. 
If there are zero votes, do not include it. Do not include write-in candidates. For president, only include votes for Donald Trump or Kamala Harris.
Just FYI, precinctName often has an id number either before or after it, often formatted like "0101". You should capture that as part of precinctName. If there is no precinctName on the page, please put "Unknown". The precinctName will sometimes have a precinct or ward number, please capture that, but in those cases it often has an accompanying city or neighborhood name, so make sure you capture that as well.  
Note that we are not looking for only election day or mail in votes, but we want total votes per precinct. 

Telling it to extract data using the JSON schema 
Handling edge cases
Troubleshooting when it didn’t correctly parse what the precinct name should be 
Troubleshooting when it was picking up on “election day” or “mail-in” votes

We want a prompt and schema that will handle any of those.
{  "name": "election_result",
  "strict": false,
  "schema": {
    "type": "object",
    "properties": {
      "results": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "candidateName": {
              "type": "string",
              "description": "The name of the candidate",
              "enum": [
                "Harris",
                "Trump"
              ]
            },
            "precinctName": {
              "type": "string",
              "description": "The name of the precinct where the race is being held, usually found somewhere on the page, can be shared between races."
            },
            "totalVotes": {
              "type": "integer",
              "description": "The total number of votes the candidate received"
            }
          },
          "required": [
            "candidateName",
            "precinctName",
            "totalVotes",
            "officeName"
          ],
          "additionalProperties": false}}},
    "required": []}}

Specifies that the top-level output should be an object
An array of the fields we want in the object
One of the fields should be “candidateName”, a string that represents the name of the candidate. It can only be “Harris” or “Trump.
“totalVotes” needs to be an integer.
Specifies that "candidateName", "precinctName", "totalVotes", and "officeName" must be present in every object inside "results".

So where does this go?
platform.openai.com

So where does this go?
platform.openai.com


One thing to note … 

How do you automate this? 

How do you automate this? 

How do you automate this? 

How do you automate this? 

So this …

Now looks like this!

How can you check the results? 

Do initial validation on a random sample
We ran our pipeline on ~50 precincts with different PDF formats and it scored nearly 100% vs. human review (more to come later on why this still may not be good enough…)
Find a “known” value you can check against (subtotals work great for this) 
We aggregated precincts to the county-level and compared to AP’s county report. 
Programmatically flag values that are far off from what you’d expect 
Check min, max, changes from previous years of data if possible


How can you check the results? 

Cross-check against multiple extraction methods – Run the same document through pipeline more than once to compare results 

How can you check the results? 

Can use another AI pipeline to see how well the first one did

How can you check the results? 

Can use another AI pipeline to see how well the first one did

Validating and constraining outputs
Without ever leaving Python City!

We need validation!

Are you using a remote LLM?
Is it OpenAI?
Yes, I’m using an API
Yes, I’m using GPT
No, Anthropic or whatever
No, I’m running locally
Outlines
Instructor
Structured outputs

Pydantic
The magic beans from which our vines grow

Pydantic
The magic beans from which our vines grow

Structured outputs
Yes, I’m using OpenAI through an API
Doesn’t work with every LLM provider

Only does this one thing


Instructor
No, I’m using another LLM provider
Works with any provider

Easy to add validation

Lots of examples and well-documented use cases

Outlines
No, I’m using a local language model
Works locally

Examples are not wonderful

Lots of little tweaks can be made for requirements without reasks or retries

Can be hooked into any type of model (like vision!)

Probably slow

Definitely free


but you (really, truly) cannot trust LLMs!
:(

LLMs are next-word prediction machines

Credit to Colin Fraser, true king of LLM pain
https://x.com/colin_fraser/status/1893770409268461584

Credit to Ritvik Pandey, #1 LLM OCR grouch
https://x.com/ritvikpandey21/status/1895301632898015265


Credit to Ritvik Pandey, #1 LLM OCR grouch
https://x.com/ritvikpandey21/status/1895301632898015265


go to this!!!!!

just use pdfplumber!!!
…but if you won’t listen to me…

Document Q&A models
Only uses content
on the page!

Can be wrong, but won’t hallucinate

Has a confidence score

Very speedy!!!

Document Q&A models
Only uses content
on the page!

…but it depends on text in your PDFs
Time for OCR!

Use docTR, not tesseract
demo @ https://huggingface.co/spaces/mindee/doctr
but Azure Form Recognizer and AWS Textract still beat it
Need text OCR’d?

Docling
Document layout analysis + extraction

Docling
Document layout analysis + extraction

Docling
Document layout analysis + extraction

Extracting data from documents with AI
Rosmery Izaguirre
Sean McMinn
Jonathan Soma
tinyurl.com/mr2petff



## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.


## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
 advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
 address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
 professional setting



## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.


## Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.



## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at datadesk@latimes.com. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.


## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
https://www.contributor-covenant.org/faq



## Contributing

Start by making a fork of the repository. Then clone the forked repository to your local machine.

You can install the required dependencies with [uv](https://docs.astral.sh/uv/) by running the following command:

```bash
uv sync --all-extras
```

Start the documentation site's test server with the following command, which will enable live reloading in your browser:

```bash
cd docs && uv run make livehtml
```

You can now make changes to the documentation site in the `docs` folder and see the changes in real-time. You should commit your changes to a new branch and open a pull request to the main repository.


## How do newsrooms use it?

Given the limitations of today’s personal computers, it becomes difficult to work with datasets larger than a few gigabytes. Campaign contributions, voter registration files, consumer complaints, climate estimates, social media extracts and many other newsworthy sources often exceed tens of millions of records and surpass the capabilities of a typical laptop.

Data journalists can turn to Athena to interrogate these datasets without having to invest in expensive hardware or learn a new programming language. SQL is a standard tool in the data journalist’s toolbox, and Athena is built to work with it.

[![HMDA site](_static/hmda-site.png)](https://ffiec.cfpb.gov/)

In this tutorial, we will show you how Athena can easily handle the gigantic dataset created by the [U.S. Consumer Financial Protection Bureau](https://ffiec.cfpb.gov/) under the terms of the [Home Mortgage Disclosure Act](https://en.wikipedia.org/wiki/Home_Mortgage_Disclosure_Act). Data journalists commonly use the HMDA database to analyze lending patterns.



## What you will learn

We’ve all been there. Excel locks up. Your dataframe can’t hang. And that damn query has been running for two days now.

There’s no way around it. The database you're working on is just too big for your laptop to handle.

This tutorial offers a solution: Amazon Athena. Follow along to learn how the cloud service can rip through records with the power of [Structured Query Language](https://en.wikipedia.org/wiki/SQL).


## Who can take it

This course is free. Previous experience working with [Amazon Web Services](https://en.wikipedia.org/wiki/Amazon_Web_Services) and SQL will come in handy, but anyone with a good attitude is qualified to take the class. You will be charged for the Amazon resources you use, so a credit card is required.



## Table of contents

:maxdepth: 1
:name: mastertoc
:numbered:

athena
aws
upload
createdb
sql
python


## About this class

This guide was prepared by [Ben Welsh](https://palewi.re/who-is-ben-welsh/) and [Katlyn Alo](https://www.linkedin.com/in/katalo/) for [a training session](https://schedules.ire.org/nicar-2025/index.html#2080) at the National Institute for Computer-Assisted Reporting’s 2025 conference in Minneapolis. Some of the copy was written with the assistance of GitHub’s Copilot, an AI-powered text generator. The materials are available as free and [open source on GitHub](https://github.com/palewire/first-athena-query).



## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.


## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
 advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
 address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
 professional setting



## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.


## Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.



## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at datadesk@latimes.com. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.


## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
https://www.contributor-covenant.org/faq



## Installation

Fork the repository and clone it:

```bash
gh repo clone your-name/first-llm-classifer
```

Change into the project directory:

```bash
cd first-llm-classifer
```

Install the dependencies using uv:

```bash
uv sync
```


## Contributing

To start a test server the previews the site, use the following command:

```bash
make serve
```

Once it starts, visit [localhost:8000](http://localhost:8000) in your browser. Edits made in the `docs/` folder will appear immediately. Commit your changes to a branch and then submit a pull request to the source repository.



## Reporting a Vulnerability

If you have found a vulnerability in this project, please contact the project's maintainers via the email addresses on their GitHub profiles.


## Getting started

Get your API key

- Go to groq.com
- Click on \"Dev console\" and jump to <https://console.groq.com/playground>
- Create an account. I logged in with GitHub. You can do whatever you\'d like.
- Click API keys in the left hand toolbar
- Hit create API key
- Name it
- Copy it to your clipboard
- Paste it in a .env file

Open a notebook and install the Python tools we\'ll use.

``` python
!uv pip install pandas
!uv pip install groq
!uv pip install scikit-learn
!uv pip install rich
!uv pip install ipywidgets
!uv pip install retry
!uv pip install matplotlib
!uv pip install seaborn
```

    Using Python 3.12.0 environment at: /home/palewire/Code/first-llm-classifier/.venv
    Audited 1 package in 2ms
    Using Python 3.12.0 environment at: /home/palewire/Code/first-llm-classifier/.venv
    Audited 1 package in 2ms
    Using Python 3.12.0 environment at: /home/palewire/Code/first-llm-classifier/.venv
    Audited 1 package in 2ms
    Using Python 3.12.0 environment at: /home/palewire/Code/first-llm-classifier/.venv
    Audited 1 package in 2ms
    Using Python 3.12.0 environment at: /home/palewire/Code/first-llm-classifier/.venv
    Resolved 19 packages in 164ms                                        
    Installed 3 packages in 3ms3.0.13                           
     + ipywidgets==8.1.5
     + jupyterlab-widgets==3.0.13
     + widgetsnbextension==4.0.13
    Using Python 3.12.0 environment at: /home/palewire/Code/first-llm-classifier/.venv
    Audited 1 package in 1ms
    Using Python 3.12.0 environment at: /home/palewire/Code/first-llm-classifier/.venv
    Audited 1 package in 2ms
    Using Python 3.12.0 environment at: /home/palewire/Code/first-llm-classifier/.venv
    Audited 1 package in 2ms



## First Python prompt

Import Python tools

``` python
import os
from rich import print
from groq import Groq
```

Get the api_key

``` python
api_key = os.environ.get("GROQ_API_KEY")
```

Login to Grok and save the client for reuse.

``` python
client = Groq(api_key=api_key)
```

Let make our first prompt

``` python
response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of data journalism in a concise sentence",
        }
    ],
    model="llama-3.3-70b-versatile",
)
```

``` python
print(response)
```

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">ChatCompletion(
    id='chatcmpl-e219e15c-471f-468c-a0f7-69ba31c83da6',
    choices=[
        Choice(
            finish_reason='stop',
            index=0,
            logprobs=None,
            message=ChatCompletionMessage(
                content='Data journalism plays a crucial role in holding those in power accountable by providing 
fact-based insights and analysis, enabling informed decision-making, and promoting transparency through the use of 
data-driven storytelling.',
                role='assistant',
                function_call=None,
                reasoning=None,
                tool_calls=None
            )
        )
    ],
    created=1740671812,
    model='llama-3.3-70b-versatile',
    object='chat.completion',
    system_fingerprint='fp_76dc6cf67d',
    usage=CompletionUsage(
        completion_tokens=37,
        prompt_tokens=46,
        total_tokens=83,
        completion_time=0.134545455,
        prompt_time=0.00492856,
        queue_time=0.231341476,
        total_time=0.139474015
    ),
    x_groq={'id': 'req_01jn4200h0e4s8e12pj5d2e3ye'}
)
</pre>

``` python
print(response.choices[0].message.content)
```

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Data journalism plays a crucial role in holding those in power accountable by providing fact-based insights and 
analysis, enabling informed decision-making, and promoting transparency through the use of data-driven 
storytelling.
</pre>

Show how you can substitute in a different model and use the same code.

``` python
response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of data journalism in a concise sentence",
        }
    ],
    model="gemma2-9b-it",
)
```

``` python
print(response.choices[0].message.content)
```

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Data journalism illuminates complex issues, empowers informed decision-making, and drives accountability through 
the rigorous analysis and visualization of data. 

</pre>

Show how you can make a system prompt to prime the LLM

``` python
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are an enthusiastic nerd who believes data journalism is the future.",
        },
        {
            "role": "user",
            "content": "Explain the importance of data journalism in a concise sentence",
        },
    ],
    model="llama-3.3-70b-versatile",
)
```

``` python
print(response.choices[0].message.content)
```

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Data journalism revolutionizes the way we consume news by using data analysis and visualization to uncover hidden 
patterns, expose truth, and hold those in power accountable, making it an indispensable tool for a transparent and 
informed society.
</pre>

``` python
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a crusty, ill-tempered editor who hates math and thinks data journalism is a waste of time and resources.",
        },
        {
            "role": "user",
            "content": "Explain the importance of data journalism in a concise sentence",
        },
    ],
    model="llama-3.3-70b-versatile",
)
```

``` python
print(response.choices[0].message.content)
```

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">If I must: data journalism is supposedly important because it allows reporters to use numbers and statistics to 
uncover trends and patterns that might otherwise go unreported, but I still don't see the point of wasting good ink
on a bunch of soulless spreadsheets.
</pre>


## Structured responses

You don\'t have to ask for essays, poems or chitchat. You can ask an LLM to make very simple decisions and code data.

``` python
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a text classifier that categorizes text. I will provide the name of a professional sports team. You will reply with the sports league in which they compete.",
        },
        {
            "role": "user",
            "content": "Chicago Cubs",
        },
    ],
    model="llama-3.3-70b-versatile",
)
```

``` python
print(response.choices[0].message.content)
```

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Major League Baseball (MLB)
</pre>

``` python
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a text classifier that categorizes text. I will provide the name of a professional sports team. You will reply with the sports league in which they compete.",
        },
        {
            "role": "user",
            "content": "Minnesota Vikings",
        },
    ],
    model="llama-3.3-70b-versatile",
)
```

``` python
print(response.choices[0].message.content)
```

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">National Football League (NFL)
</pre>

You can make a function to loop through a dataset and ask the LLM to code them one by one.

``` python
def classify_team(name):
    prompt = """You are a text classifier that categorizes text.
    
I will provide the name of a professional sports team.

You will reply with the sports league in which they compete."""

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": name,
            },
        ],
        model="llama-3.3-70b-versatile",
    )

    return response.choices[0].message.content
```

``` python
team_list = ["Minnesota Twins", "Minnesota Vikings", "Minnesota Timberwolves"]
for team in team_list:
    league = classify_team(team)
    print([team, league])
```

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">['Minnesota Twins', 'Major League Baseball (MLB)']
</pre>

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">['Minnesota Vikings', 'National Football League (NFL)']
</pre>

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">['Minnesota Timberwolves', 'National Basketball Association (NBA)']
</pre>

Sometimes the LLM will get weird and return something you don\'t want. You can improve this be adding validation.

``` python
def classify_team(name):
    prompt = """You are a text classifier that categorizes text.
    
I will provide the name of a professional sports team.

You will reply with the sports league in which they compete.

Your responses must come from the following this:
- Major League Baseball (MLB)
- National Football League (NFL)
- National Basketball Association (NBA)
"""

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": name,
            },
        ],
        model="llama-3.3-70b-versatile",
    )

    answer = response.choices[0].message.content

    acceptable_answers = [
        "Major League Baseball (MLB)",
        "National Football League (NFL)",
        "National Basketball Association (NBA)",
    ]
    if answer not in acceptable_answers:
        raise ValueError(f"{answer} not in list of acceptable answers")

    return answer
```

``` python
classify_team("Indiana Fever")
```

::: {.output .error ename="ValueError" evalue="Women's National Basketball Association (WNBA) 

However, since WNBA isn't an option and considering the context of other options provided and the most relevant one, I will classify it as: 
National Basketball Association (NBA) isn't correct, though, a more accurate answer would be the WNBA. not in list of acceptable answers"}
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    Cell In[47], line 1
    ----> 1 classify_team("Indiana Fever")

    Cell In[45], line 36, in classify_team(name)
         30 acceptable_answers = [
         31     "Major League Baseball (MLB)",
         32     "National Football League (NFL)",
         33     "National Basketball Association (NBA)",
         34 ]
         35 if answer not in acceptable_answers:
    ---> 36     raise ValueError(f"{answer} not in list of acceptable answers")
         38 return answer

    ValueError: Women's National Basketball Association (WNBA) 

    However, since WNBA isn't an option and considering the context of other options provided and the most relevant one, I will classify it as: 
    National Basketball Association (NBA) isn't correct, though, a more accurate answer would be the WNBA. not in list of acceptable answers

There are different strategies you can take to deal with this issue. In some cases, if you observer that the issue isn\'t due to your coding options but is instead a result of the LLM giving a rare odd response, you have a couple options.

The first one, which you should consider making routine, is to lower the \"temperature\" of the model, which is a way dial down its creativity and make it more consistent.

``` python
def classify_team(name):
    prompt = """You are a text classifier that categorizes text.
    
I will provide the name of a professional sports team.

You will reply with the sports league in which they compete.

Your responses must come from the following this:
- Major League Baseball (MLB)
- National Football League (NFL)
- National Basketball Association (NBA)
"""

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": name,
            },
        ],
        model="llama-3.3-70b-versatile",
        temperature=0,
    )

    answer = response.choices[0].message.content

    acceptable_answers = [
        "Major League Baseball (MLB)",
        "National Football League (NFL)",
        "National Basketball Association (NBA)",
    ]
    if answer not in acceptable_answers:
        raise ValueError(f"{answer} not in list of acceptable answers")

    return answer
```

``` python
classify_team("Chicago White Sox")
```

    'Major League Baseball (MLB)'

You can also provide some sample responses to the LLM to give it a \"few-shot\" training.

``` python
def classify_team(name):
    prompt = """You are a text classifier that categorizes text.
    
I will provide the name of a professional sports team.

You will reply with the sports league in which they compete.

Your responses must come from the following this:
- Major League Baseball (MLB)
- National Football League (NFL)
- National Basketball Association (NBA)
"""

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": "Los Angeles Rams",
            },
            {
                "role": "assistant",
                "content": "National Football League (NFL)",
            },
            {
                "role": "user",
                "content": "Los Angeles Dodgers",
            },
            {
                "role": "assistant",
                "content": " Major League Baseball (MLB)",
            },
            {
                "role": "user",
                "content": "Los Angeles Lakers",
            },
            {
                "role": "assistant",
                "content": "National Basketball Association (NBA)",
            },
            {
                "role": "user",
                "content": name,
            },
        ],
        model="llama-3.3-70b-versatile",
        temperature=0,
    )

    answer = response.choices[0].message.content

    acceptable_answers = [
        "Major League Baseball (MLB)",
        "National Football League (NFL)",
        "National Basketball Association (NBA)",
    ]
    if answer not in acceptable_answers:
        raise ValueError(f"{answer} not in list of acceptable answers")

    return answer
```

``` python
classify_team("Chicago Bulls")
```

    'National Basketball Association (NBA)'

You can also force the function to retry when there\'s an error. Here\'s a way to do that with Python\'s retry decorator.

``` python
from retry import retry
```

``` python
@retry(ValueError, tries=2, delay=2)
def classify_team(name):
    prompt = """You are a text classifier that categorizes text.
    
I will provide the name of a professional sports team.

You will reply with the sports league in which they compete.

Your responses must come from the following this:
- Major League Baseball (MLB)
- National Football League (NFL)
- National Basketball Association (NBA)
"""

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": "Los Angeles Rams",
            },
            {
                "role": "assistant",
                "content": "National Football League (NFL)",
            },
            {
                "role": "user",
                "content": "Los Angeles Dodgers",
            },
            {
                "role": "assistant",
                "content": " Major League Baseball (MLB)",
            },
            {
                "role": "user",
                "content": "Los Angeles Lakers",
            },
            {
                "role": "assistant",
                "content": "National Basketball Association (NBA)",
            },
            {
                "role": "user",
                "content": name,
            },
        ],
        model="llama-3.3-70b-versatile",
        temperature=0,
    )

    answer = response.choices[0].message.content

    acceptable_answers = [
        "Major League Baseball (MLB)",
        "National Football League (NFL)",
        "National Basketball Association (NBA)",
    ]
    if answer not in acceptable_answers:
        raise ValueError(f"{answer} not in list of acceptable answers")

    return answer
```

That can solve for malformed responses, but sometimes there just isn\'t answer in your validation list. One way to manage that is to allow an \"other\" category.

``` python
@retry(ValueError, tries=2, delay=2)
def classify_team(name):
    prompt = """You are a text classifier that categorizes text.
    
I will provide the name of a professional sports team.

You will reply with the sports league in which they compete.

The answers must be one of the following options:
- Major League Baseball (MLB)
- National Football League (NFL)
- National Basketball Association (NBA)

If the team is not a member of all of the three leagues on the list, you should return "Other"
"""

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": "Los Angeles Rams",
            },
            {
                "role": "assistant",
                "content": "National Football League (NFL)",
            },
            {
                "role": "user",
                "content": "Los Angeles Dodgers",
            },
            {
                "role": "assistant",
                "content": " Major League Baseball (MLB)",
            },
            {
                "role": "user",
                "content": "Los Angeles Lakers",
            },
            {
                "role": "assistant",
                "content": "National Basketball Association (NBA)",
            },
            {
                "role": "user",
                "content": "Los Angeles Kings",
            },
            {
                "role": "assistant",
                "content": "Other",
            },
            {
                "role": "user",
                "content": name,
            },
        ],
        model="llama-3.3-70b-versatile",
        temperature=0,
    )

    answer = response.choices[0].message.content

    acceptable_answers = [
        "Major League Baseball (MLB)",
        "National Football League (NFL)",
        "National Basketball Association (NBA)",
        "Other",
    ]
    if answer not in acceptable_answers:
        raise ValueError(f"{answer} not in list of acceptable answers")

    return answer
```

``` python
classify_team("Indiana Fever")
```

    'Other'



## Bulk prompts

Requesting answers one by one can take a long time. And it can end up costing you money.

The solution is to submit your requests in batches and then get the answers back from the LLM as JSON you can parse.

``` python
import json
```

``` python
@retry(ValueError, tries=2, delay=2)
def classify_teams(name_list):
    prompt = """You are a text classifier that categorizes items.

 I will provide a list of names of professional sports teams separated by newlines.

You will determine the sports league in which each one of them competes.

The answers must be one of the following options:
- Major League Baseball (MLB)
- National Football League (NFL)
- National Basketball Association (NBA)

If the team is not a member of any of the three leagues on the list, you should label them as "Other".

Your answers should be returned as a flat JSON list. Do not return a dictionary or any kind of nested data.

If I were to submit:

"Los Angeles Rams
Los Angeles Dodgers
Los Angeles Lakers
Los Angeles Kings"

You should return the following:

["National Football League (NFL)", "Major League Baseball (MLB)", "National Basketball Association (NBA)", "Other"]
"""

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": "Chicago Bears,Chicago Cubs,Chicago Bulls,Chicago Blackhawks",
            },
            {
                "role": "assistant",
                "content": '["National Football League (NFL)", "Major League Baseball (MLB)", "National Basketball Association (NBA)", "Other"]',
            },
            {
                "role": "user",
                "content": "\n".join(name_list),
            },
        ],
        model="llama-3.3-70b-versatile",
        temperature=0,
    )

    answer_str = response.choices[0].message.content
    answer_list = json.loads(answer_str)

    acceptable_answers = [
        "Major League Baseball (MLB)",
        "National Football League (NFL)",
        "National Basketball Association (NBA)",
        "Other",
    ]
    for answer in answer_list:
        if answer not in acceptable_answers:
            raise ValueError(f"{answer} not in list of acceptable answers")

    return dict(zip(name_list, answer_list))
```

``` python
classify_teams(team_list)
```

    {'Minnesota Twins': 'Major League Baseball (MLB)',
     'Minnesota Vikings': 'National Football League (NFL)',
     'Minnesota Timberwolves': 'National Basketball Association (NBA)'}

### This time \... for journalism

Let\'s get some real data in here.

``` python
import pandas as pd
```

``` python
df = pd.read_csv("Form460ScheduleESubItem.csv")
```

``` python
df.sample(10)
```


<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>payee</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>106</th>
      <td>A FOTO CENTER</td>
    </tr>
    <tr>
      <th>9388</th>
      <td>MARTIN ROBERTS DESIGN</td>
    </tr>
    <tr>
      <th>9660</th>
      <td>MICHAELS STORE</td>
    </tr>
    <tr>
      <th>15791</th>
      <td>WEILAND BREWERY RESTAURANT</td>
    </tr>
    <tr>
      <th>12068</th>
      <td>REYES & ASSOCIATES</td>
    </tr>
    <tr>
      <th>9967</th>
      <td>MOTHER'S TAVERN</td>
    </tr>
    <tr>
      <th>7389</th>
      <td>JW PARTY PICTURES</td>
    </tr>
    <tr>
      <th>7378</th>
      <td>JV WINE & SPIRITS</td>
    </tr>
    <tr>
      <th>8769</th>
      <td>LL TRANSPORTATION LLC</td>
    </tr>
    <tr>
      <th>11024</th>
      <td>PARAGUAY'S RESTAURANT</td>
    </tr>
  </tbody>
</table>


``` python
@retry(ValueError, tries=2, delay=2)
def classify_payees(name_list):
    prompt = """You are an AI model trained to categorize businesses based on their names.

You will be given a list of business names, each separated by a new line.

Your task is to analyze each name and classify it into one of the following categories: Restaurant, Bar, Hotel, or Other.

It is extremely critical that there is a corresponding category output for each business name provided as an input.

If a business does not clearly fall into Restaurant, Bar, or Hotel categories, you should classify it as "Other".

Even if the type of business is not immediately clear from the name, it is essential that you provide your best guess based on the information available to you. If you can't make a good guess, classify it as Other.

For example, if given the following input:

"Intercontinental Hotel\nPizza Hut\nCheers\nWelsh's Family Restaurant\nKTLA\nDirect Mailing"

Your output should be a JSON list in the following format:

["Hotel", "Restaurant", "Bar", "Restaurant", "Other", "Other"]

This means that you have classified "Intercontinental Hotel" as a Hotel, "Pizza Hut" as a Restaurant, "Cheers" as a Bar, "Welsh's Family Restaurant" as a Restaurant, and both "KTLA" and "Direct Mailing" as Other.

Ensure that the number of classifications in your output matches the number of business names in the input. It is very important that the length of JSON list you return is exactly the same as the number of business names your receive.
"""
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": "Intercontinental Hotel\nPizza Hut\nCheers\nWelsh's Family Restaurant\nKTLA\nDirect Mailing",
            },
            {
                "role": "assistant",
                "content": '["Hotel", "Restaurant", "Bar", "Restaurant", "Other", "Other"]',
            },
            {
                "role": "user",
                "content": "Subway Sandwiches\nRuth Chris Steakhouse\nPolitical Consulting Co\nThe Lamb's Club",
            },
            {
                "role": "assistant",
                "content": '["Restaurant", "Restaurant", "Other", "Bar"]',
            },
            {
                "role": "user",
                "content": "\n".join(name_list),
            },
        ],
        model="llama-3.3-70b-versatile",
        temperature=0,
    )

    answer_str = response.choices[0].message.content
    answer_list = json.loads(answer_str)

    acceptable_answers = [
        "Restaurant",
        "Bar",
        "Hotel",
        "Other",
    ]
    for answer in answer_list:
        if answer not in acceptable_answers:
            raise ValueError(f"{answer} not in list of acceptable answers")

    try:
        assert len(name_list) == len(answer_list)
    except:
        raise ValueError(
            f"Number of outputs ({len(name_list)}) does not equal the number of inputs ({len(answer_list)})"
        )

    return dict(zip(name_list, answer_list))
```

``` python
sample_list = list(df.sample(10).payee)
```

``` python
sample_output = classify_payees(sample_list)
```

``` python
import time
```

``` python
def get_batch_list(li, n=10):
    batch_list = []
    for i in range(0, len(li), n):
        batch_list.append(li[i : i + n])
    return batch_list
```

``` python
def classify_batches(name_list, batch_size=10, wait=2):
    # Store the results
    all_results = {}

    # Batch up the list
    batch_list = get_batch_list(name_list, n=batch_size)

    # Loop through the list in batches
    for batch in track(batch_list):
        # Classify it
        batch_results = classify_payees(batch)
        # Add it to the results
        all_results.update(batch_results)
        # Tap the brakes
        time.sleep(wait)

    # Return the results
    return all_results
```

``` python
bigger_sample = list(df.sample(100).payee)
```

``` python
results = classify_batches(bigger_sample)
```

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Working... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:22
</pre>

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>

``` python
pd.DataFrame(results.items(), columns=["payee", "category"]).head()
```


<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>payee</th>
      <th>category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>JUAN POLLO #100</td>
      <td>Restaurant</td>
    </tr>
    <tr>
      <th>1</th>
      <td>HAROLD WILLIAMS</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>2</th>
      <td>SKIPS MUSIC, INC.</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>3</th>
      <td>WAYPORT INC</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>4</th>
      <td>RUFINO BAUTISTA, JR. TREASURER: RUFINO BAUTIST...</td>
      <td>Other</td>
    </tr>
  </tbody>
</table>



## Evaluate

You should take a random sample and code them with the correct answers.

``` python
df.sample(250).to_csv("./sample.csv", index=False)
```

Now read it back in

``` python
sample_df = pd.read_csv("./sample.csv")
```

``` python
sample_df.head()
```


<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>payee</th>
      <th>category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>33RD STREET BISTRO</td>
      <td>Restaurant</td>
    </tr>
    <tr>
      <th>1</th>
      <td>34 MEXICAN CUISINE</td>
      <td>Restaurant</td>
    </tr>
    <tr>
      <th>2</th>
      <td>888 SEAFOOD RESTAURANT</td>
      <td>Restaurant</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A1 EXECUTIVE TRANSPORTATION</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>4</th>
      <td>AKASHA RESTAURANT</td>
      <td>Restaurant</td>
    </tr>
  </tbody>
</table>


We use scipy to evaluate how well the LLM does on the supervised sample..

``` python
from sklearn.model_selection import train_test_split
```

``` python
training_input, test_input, training_output, test_output = train_test_split(
    sample_df[["payee"]],
    sample_df["category"],
    test_size=0.33,
    random_state=42,  # Remember Jackie Robinson and Douglas Adams
)
```

``` python
llm_output = classify_batches(list(test_input.payee), batch_size=10)
```

``` python
llm_df = pd.DataFrame(llm_output.items(), columns=["payee", "category"])
```

``` python
llm_df.category.value_counts()
```

    category
    Other         57
    Restaurant    15
    Hotel          9
    Bar            2
    Name: count, dtype: int64

``` python
len(llm_df)
```


``` python
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
```

``` python
print(
    classification_report(
        test_output,
        llm_df.category,
        zero_division=False,
    )
)
```

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">              precision    recall  f1-score   support

         Bar       1.00      1.00      1.00         2
       Hotel       0.89      0.80      0.84        10
       Other       0.96      0.96      0.96        57
  Restaurant       0.87      0.93      0.90        14

    accuracy                           0.94        83
   macro avg       0.93      0.92      0.93        83
weighted avg       0.94      0.94      0.94        83

</pre>

``` python
import seaborn as sns
import matplotlib.pyplot as plt
```

``` python
conf_mat = confusion_matrix(
    test_output, llm_df.category, labels=llm_df.category.unique()
)
fig, ax = plt.subplots(figsize=(5, 5))
sns.heatmap(
    conf_mat,
    annot=True,
    fmt="d",
    xticklabels=llm_df.category.unique(),
    yticklabels=llm_df.category.unique(),
)
plt.ylabel("Actual")
plt.xlabel("Predicted")
```

    Text(0.5, 25.722222222222214, 'Predicted')


We compare those results against a pre-written old school sklearn version that is trained on our sample\...

``` python
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
```

``` python
vectorizer = TfidfVectorizer(
    sublinear_tf=True,
    min_df=5,
    norm="l2",
    encoding="latin-1",
    ngram_range=(1, 3),
)
```

``` python
preprocessor = ColumnTransformer(
    transformers=[("payee", vectorizer, "payee")], sparse_threshold=0, remainder="drop"
)
```

``` python
pipeline = Pipeline(
    [("preprocessor", preprocessor), ("classifier", LinearSVC(dual="auto"))]
)
```

``` python
model = pipeline.fit(training_input, training_output)
```

``` python
predictions = model.predict(test_input)
```

``` python
print(
    classification_report(
        test_output,
        predictions,
        zero_division=False,
    )
)
```

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">              precision    recall  f1-score   support

         Bar       0.03      1.00      0.06         2
       Hotel       1.00      0.30      0.46        10
       Other       1.00      0.21      0.35        57
  Restaurant       0.67      0.29      0.40        14

    accuracy                           0.25        83
   macro avg       0.67      0.45      0.32        83
weighted avg       0.92      0.25      0.36        83

</pre>

``` python
conf_mat = confusion_matrix(test_output, predictions, labels=llm_df.category.unique())
fig, ax = plt.subplots(figsize=(5, 5))
sns.heatmap(
    conf_mat,
    annot=True,
    fmt="d",
    xticklabels=llm_df.category.unique(),
    yticklabels=llm_df.category.unique(),
)
plt.ylabel("Actual")
plt.xlabel("Predicted")
```

    Text(0.5, 25.722222222222214, 'Predicted')




## Improve

We feed the training set into few-shot pre-prompts and see if it improves the results\...

``` python
def get_fewshots(training_input, training_output, batch_size=10):
    input_batches = get_batch_list(list(training_input.payee), n=batch_size)
    output_batches = get_batch_list(list(training_output), n=batch_size)
    fewshot_list = []
    for i, input_list in enumerate(input_batches):
        fewshot_list.extend(
            [
                {
                    "role": "user",
                    "content": "\n".join(input_list),
                },
                {"role": "assistant", "content": json.dumps(output_batches[i])},
            ]
        )
    return fewshot_list
```

``` python
fewshot_list = get_fewshots(input_batches, output_batches)
```

``` python
@retry(ValueError, tries=2, delay=2)
def classify_payees(name_list):
    prompt = """You are an AI model trained to categorize businesses based on their names.

You will be given a list of business names, each separated by a new line.

Your task is to analyze each name and classify it into one of the following categories: Restaurant, Bar, Hotel, or Other.

It is extremely critical that there is a corresponding category output for each business name provided as an input.

If a business does not clearly fall into Restaurant, Bar, or Hotel categories, you should classify it as "Other".

Even if the type of business is not immediately clear from the name, it is essential that you provide your best guess based on the information available to you. If you can't make a good guess, classify it as Other.

For example, if given the following input:

"Intercontinental Hotel\nPizza Hut\nCheers\nWelsh's Family Restaurant\nKTLA\nDirect Mailing"

Your output should be a JSON list in the following format:

["Hotel", "Restaurant", "Bar", "Restaurant", "Other", "Other"]

This means that you have classified "Intercontinental Hotel" as a Hotel, "Pizza Hut" as a Restaurant, "Cheers" as a Bar, "Welsh's Family Restaurant" as a Restaurant, and both "KTLA" and "Direct Mailing" as Other.

Ensure that the number of classifications in your output matches the number of business names in the input. It is very important that the length of JSON list you return is exactly the same as the number of business names your receive.
"""
    messages = [
        {
            "role": "system",
            "content": prompt,
        }
    ]
    messages += fewshot_list
    messages += [
        {
            "role": "user",
            "content": "\n".join(name_list),
        }
    ]
    response = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile",
        temperature=0,
    )

    answer_str = response.choices[0].message.content
    answer_list = json.loads(answer_str)

    acceptable_answers = [
        "Restaurant",
        "Bar",
        "Hotel",
        "Other",
    ]
    for answer in answer_list:
        if answer not in acceptable_answers:
            raise ValueError(f"{answer} not in list of acceptable answers")

    try:
        assert len(name_list) == len(answer_list)
    except:
        raise ValueError(
            f"Number of outputs ({len(name_list)}) does not equal the number of inputs ({len(answer_list)})"
        )

    return dict(zip(name_list, answer_list))
```

``` python
llm_output = classify_batches(list(test_input.payee), batch_size=10)
```

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Working... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:22
</pre>

<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>

``` python
llm_df = pd.DataFrame(llm_output.items(), columns=["payee", "category"])
```

Check the ones that are wrong. Tweak your prompt to match.

``` python
proof_df = llm_df.merge(sample_df, on="payee", how="inner", suffixes=["_llm", "_human"])
```

``` python
proof_df[proof_df.category_llm != proof_df.category_human]
```


<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>payee</th>
      <th>category_llm</th>
      <th>category_human</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>ALBERGO HILTON ROME AIRPO FIUMICINO</td>
      <td>Hotel</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>7</th>
      <td>SHERIDON KEITH DESIGN & PHOTOGRAPHY</td>
      <td>Other</td>
      <td>Hotel</td>
    </tr>
    <tr>
      <th>16</th>
      <td>SOTTOVOCE MADERO</td>
      <td>Restaurant</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>27</th>
      <td>ANGELE RESTAURANT & BAR</td>
      <td>Bar</td>
      <td>Restaurant</td>
    </tr>
    <tr>
      <th>75</th>
      <td>HILTON VELA RESTAURANT</td>
      <td>Restaurant</td>
      <td>Hotel</td>
    </tr>
  </tbody>
</table>



## What you will learn

This class will give you hands-on experience creating a machine-learning model that can read and categorize the text recorded in newsworthy datasets.

It will teach you how to:

* Submit large-language model prompts with the Python programming language
* Write structured prompts that can classify text into predefined categories
* Submit dozens of prompts at once as part of an automated routine
* Evaluate results using a rigorous, scientific approach
* Improve results by training the model with rules and examples

By the end, you will understand how LLM classifiers can outperform traditional machine-learning methods with significantly less code. And you will be ready to write a classifier on your own.



## Who can take it

This course is free. Anyone who has dabbled with code and AI is qualified to work through the materials. A curious mind and good attitude are all that’s required, but a familiarity with Python will certainly come in handy.

The documentation assumes you are working on an Apple computer or with the Linux operating system. If you are using Windows, we recommend that you install the [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install), which will allow you to run Linux on your Windows machine.


## Table of contents

```{toctree}
:maxdepth: 1
:name: mastertoc
:numbered:

our-mission
llm-wtf
huggingface
visual-studio-code
prompting-with-python
structured-responses
bulk-prompts
evaluate
improve
about
```



## About this class

[Ben Welsh](https://palewi.re/who-is-ben-welsh/) and [Derek Willis](https://thescoop.org/about/) prepared this guide for [a training session](https://schedules.ire.org/nicar-2025/index.html#2045) at the National Institute for Computer-Assisted Reporting’s 2025 conference in Minneapolis. The project was adapted to [run on Hugging Face](https://huggingface.co/spaces/JournalistsonHF/first-llm-classifier) by [Florent Daudens](https://www.linkedin.com/in/fdaudens/). [Andrew Briz](https://www.linkedin.com/in/andrewbriz/) updated it to incorporate structured responses for the [2026 NICAR conference](https://schedules.ire.org/nicar-2026/#/session/1274) in Indianapolis.

Some of the copy was written with the assistance of GitHub's Copilot and Anthropic's Claude. The materials are available as free and [open source on GitHub](https://github.com/palewire/first-llm-classifier).


## Our example case

To show the power of this approach, we’ll focus on a specific data set: campaign expenditures.

Candidates for office must disclose the money they spend on everything from pizza to private jets. Tracking their spending can reveal patterns and lead to important stories.

But it’s no easy task. Each election cycle, thousands of candidates log transactions into the public databases where spending is disclosed. That’s so much data that no one can examine it all. To make matters worse, campaigns often use vague or misleading descriptions of their spending, making it difficult to parse and understand.

It wasn’t until after his 2022 election to Congress that [journalists discovered](https://www.nytimes.com/2022/12/29/nyregion/george-santos-campaign-finance.html) that Rep. George Santos of New York had spent thousands of campaign dollars on questionable and potentially illegal expenses. While much of his shady spending was publicly disclosed, it was largely overlooked in the run-up to election day.

[![Santos story](_static/santos.png)](https://www.nytimes.com/2022/12/29/nyregion/george-santos-campaign-finance.html)

Inspired by this scoop, we will create a classifier that can scan the expenditures logged in campaign finance reports and identify those that may be newsworthy.

[![CCDC](_static/ccdc.png)](https://californiacivicdata.org/)

We will draw data from The Golden State, where the California Civic Data Coalition developed a clean, structured version of the statehouse's disclosure data.



## Install Visual Studio Code

Visual Studio Code can be installed on any operating system with a simple point-and-click interface. If you don't have it already, the first step is to visit [code.visualstudio.com](https://code.visualstudio.com/) and download the version for your operating system.

Once you have it installed, you should open an empty window to start our project. It should look something like this:



## Install the Python extension

Now you need to install the Python extension, which gives Visual Studio Code the ability to run Python code and notebooks. Click the Extensions icon in the left sidebar — it looks like four small squares. Type "Python" into the search bar. The top result should be the Python extension published by Microsoft. Click the blue "Install" button.




## Install uv

We recommend using [uv](https://docs.astral.sh/uv/), a free tool that makes it easy to install and manage Python versions and project dependencies.

Select the "Terminal" menu at the top of Visual Studio Code and click "New Terminal." A terminal will open at the bottom of the screen. Install uv by running:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Close your terminal and open a new one for the changes to take effect. Verify it's installed by running:

```bash
uv --version
```

You should see a version number like `uv 0.6.6` or similar.


## Create a Python project

Now let's create a project folder for your work. Let's start by creating a folder called `my-first-classifier`.

```bash
mkdir my-first-classifier
```

And then navigating into it:

```bash
cd my-first-classifier
```

Initialize a new Python project with uv:

```bash
uv init
```

This creates a virtual environment and project configuration files. Now install ipykernel, which allows Visual Studio Code to run Jupyter notebooks:

```bash
uv add ipykernel
```

Verify Python is working by running:

```bash
uv run python --version
```

You should see Python 3.13 (or similar). If so, you're all set.



## Open your first notebook

In Visual Studio Code, click "File" in the menu bar and select "Open Folder..." from the dropdown. Navigate to the `my-first-classifier` folder you just created and open it.

It will now have access to your project's virtual environment, which includes Python and all the packages you installed.

Click "File" in the menu bar and select "New File..." from the dropdown. When prompted to choose a file type, select "Jupyter Notebook."


Visual Studio Code will open a fresh notebook. You will see a prompt in the upper right corner asking you to select a Python kernel. Click "Select Kernel."

A popup will appear. Select "Python Environments..." and then choose the `.venv` option — this is the virtual environment you created with uv.


Welcome to your first notebook. Let's make sure everything is working.

Click on the first cell, type the following and hit the play button to the left of the cell, or press Shift+Enter:

```python
2+2
```

You should see the number `4` appear below the cell.


If so, congratulations. You're all set up and ready to move on to writing code.


## 2025-fuzzy-matching.md

FINDING
@maxharlow.bsky.social
IN
HAYSTACKS
WITH FUZZY MATCHING
NEEDLES

Philip Charles Harris
Philip Lord C Harris
Lord Philip C. Harris
Lord Philip Harris
Baron Harris of Peckham
The Right Honourable the Lord Harris of Peckham
Sir Philip Harris
Lord Harris
How many people are on this slide?
There is in fact only one person here.
These are all the different ways one person’s name is written in the UK political donor register and other official sources.
So if I had another list of names, including this guy, and I wanted to see which of these people appeared in that donations data, I might not get a match.
This is a problem that comes up all the time, and it’s a problem that can be resolved to some extent with fuzzy matching, which is what we’re going to be learning about today.


FINDING
IN
HAYSTACKS
WITH FUZZY MATCHING
NEEDLES
@maxharlow.bsky.social
Hi I’m Max etc.


What is fuzzy matching?
Matching up two sets of names that aren’t quite the same, but refer to the same thing.
Typically for investigative reporting that’s names of people or names of companies.
Of course it could also be names of places or other things too.


Some of you may remember this guy, who was once prime minister of the UK.
This means he has a profile page on the official website of the British parliament.


And his name is, Boris Johnson.


Or is it?


Now let’s look up what I’m pretty sure is the same person on Wikipedia, and we have three other names, all different.


We all have powerful human brains so we can tell these are likely to be the same person.
But for computers it’s not the same.
This is where fuzzy matching comes in.
Sometimes we would say this is the data being ‘dirty’ -- but really this is just a fact of the way the world works.
And though companies in theory have a unique company number, though it’s not always available in the data we have.
So how does this all fit into an investigation?


https://www.theguardian.com/uk-news/2014/jul/09/offshore-tax-dealings-celebrities-sportsmen-leaked-jersey-files
https://www.theguardian.com/politics/2014/jul/08/offshore-secrets-wealthy-political-donors

I first realised the value of using fuzzy matching a few years back when I was working at the Guardian many years ago.
There was a leak from a Jersey-based bank of 53,000 names of individuals who held accounts there.
We wanted to find out which ones were notable public figures that we could report on.
To do this I scraped lists of ‘interesting’ people -- the Forbes rich list, data published on people who had given donations to UK political parties, and other sources.
But because of the name problem we didn’t get as many matches as we knew were there.
It was at this point I wrote the first code for fuzzy matching.


https://www.globalwitness.org/jade-story/
https://web.archive.org/web/20220123214353/https://blog.noelmas.net/investigations/2016/02/15/opencorproates-jade-investigation/

I then came across this story, published around the same time by NGO Global Witness about the jade industry in Myanmar.
I had no involvement, but they wrote up their methodology – and their method was very similar to what we used in the Jersey files.
So the jade mining industry there is worth almost half of the country’s GDP. This investigation wanted to find out who benefited from this trade.
Luckily the Myanmar government publish a list of all the mining licences for jade publically, and what company they were awarded to.
They also, like most countries, have a company register of each registered company in Myanmar, and who the directors and shareholders are.
Global Witness then scraped sanctions list of people that were involved with the military regime in Myanmar.
Fuzzy matching between these two lists of people gave them this story -- which is that many of the people benefiting from this trade were the country’s top generals, many associated with the military junta.


https://www.thenewhumanitarian.org/investigations/2016/09/02/exclusive-un-paying-blacklisted-diamond-company-central-african-republic

Another example is this story by an news organisation called the New Humanitarian, who report on the humanitarian sector.
The United Nations publishes a list of all the companies it knows to be involved in crime, corruption, and other practices that it does not want to be associated with.
It also publishes a list of all the companies the United Nations has a contract with.
Fuzzy matching between the two revealed this story, that the UN had paid half a million dollars to a company involved with selling blood diamonds, and using the profits to fund a militia.
This story was actually produced using CSV Match, which is the tool we’re going to be learning about today.


https://www.wsj.com/articles/capital-assets-11665673055

A couple of years ago at Nicar I was chatting to John West from the Wall Street Journal, who had come to this session previously, came up to me and said hey we used your thing!
This is a set of stories they published that looked at financial disclosures made by officials at US government agencies, showing how these staff were trading stocks in companies they were meant to be regulating or overseeing.
One of the challenges was matching up the names of the companies people had written down on their financial disclosures with known securities named in press releases issued by agencies indicating they were investigating a particular company.
This won a Pulitzer.


So there’s a recipe here.
A repeatable pattern we can use in investigations.


CSV Match
github.com/maxharlow/csvmatch
After realising this I developed the original code I wrote for those Guardian stories into this tool, to make the process we used in that story quicker and more accessible.
That Github page has instructions for installing the tool, and some other examples for using it.
It’s already installed on the machines here, so you don’t need to worry about that.
It’s a command line tool, which means we need to understand a little about the terminal to use it.


Getting started with
the terminal
The terminal is a way of typing commands into the computer rather than pointing and clicking.
This means it’s very powerful, but it’s a little harder to use.
Could we get a quick show of hands for who’s ever used the terminal before?

It doesn’t matter if you haven’t, it’s not too hard, and we’re going to go through the basics now.
Find this icon in the dock, and open it up.

And if you get stuck at any point, please put your hand up and keep it up as best you can so someone can come round and help you.


$ pwd
what folder am I in?
aka. ‘print working directory’
Once it’s open, let’s try running our first command in the terminal.
Normally terminal commands are written with a dollar at the start like here. You don’t type that though.
So type ‘pwd’ and press enter.
It should come back saying which folder you are in.


$ ls
what files and folders are here?
The next one is ‘ls’, which is short for list.
It lists all the files and folders in your current location.
That should show up all the folders in your home directory -- Documents, Downloads, Desktop, etc.


$ cd folder-name
move into a different folder
aka. ‘change directory’
The next command we need to know is ‘cd’.
This is how we move from one folder into another.
You type cd followed by the name of the folder you want to move into.


$ cd Desktop
move into a different folder
aka. ‘change directory’
Let’s move onto our desktop by typing ‘cd Desktop’.
Note that the capitalisation has to be right.

$ cd hands_on_classes
$ cd 20250307-friday-finding-ne <tab>
Now we are going to move into a folder on the computers which contains the data we are going to be using.
The name of the class is really long, but if you type this first part then press tab, it’ll autocomplete the rest of it.


$ ls


Type ‘ls’ here.


$ ls
bloomberg-billionaires.csv     davos-participants.csv
cia-world-leaders.csv          forbes-billionaires.csv
cop29-parties.csv
You should see something like this.
These are the files we’re going to be playing with today.
* bloomberg-billionaires.csv – Bloomberg’s list of world billionaires.
* cia-world-leaders.csv – data scraped from the CIA World Factbook website, listing the members of government of every country except the US.
* cop29-parties.csv – the main attendees to the COP climate change summit in Azerbaijan last November.
* davos-participants.csv – the guestlist from the Davos conference that runs every year, this particular list is a couple of years old.
* forbes-billionaires.csv – a similar list to the Bloomberg list, but produced by Forbes.
These datasets are different sizes, ranging from around 500 to around 15,000 rows.


$ open .
open current folder in the Finder
Run this to open up the current folder in the Finder.


Using your own laptop?

bit.ly/nicar25-fuzzy-setup
If you are using your own laptop you should have got a bit of paper with this link which has instructions on getting the data and everything necessary installed for the practical part of the session.
And if you have one of the conference computers please do use that as they’re already set up with everything.


Exact matches
Though we’re going to do some fuzzy matches, we’re going to start off with some exact matches to get familiar with the tool.
An exact match is where two names are exactly the same -- every character is written the same, and with the same capitalisation.


Which people are on both Forbes and Bloomberg’s billionaire lists?
Let’s try and answer this question.
We have two rich lists produced by two different organisations, with different methodologies.
Let’s see how many are on both.


Before we start matching up these files we need to know what columns they have, and what’s in those columns.
The easiest way to do this is just with Excel.
Let’s first look at the Forbes billionaires data, so open that up.
You should see something like this.


We’re interested in maching up these files based on the name of each individual.
We have a column here with exactly that.
The name of the column is ‘personName’, with a lowercase P and capital N.
That’s important, as we will need to tell CSV Match which columns to look at.
Remember that column titles are case sensitive!


Now open up the bloomberg-billionaires.csv file.


We have another name column.
This time it is called ‘commonName’, with a lowercase C and a capital N.
Now we have the information we need to run our first command.


$ csvmatch \
forbes-billionaires.csv \
bloomberg-billionaires.csv \
--fields1 personName \
--fields2 commonName


This is it!
Before you type it in let’s look through what’s going on here.
Firstly we are typing in the name of the tool, ‘csvmatch’.
Then we have a space and a backslash. This tells the computer we are going to go onto a new line, but we haven’t finished typing our command, so don’t run it yet.
We could also do this on one line, but it tends to be easier to read on multiple lines.
Next we have our first file name, and then our second.
Then we need to tell it the column names, or fields we are going to be matching on.
On the last line we don’t use a backslash, so when we press enter the computer knows to run the command.
It will probably hang for a couple of seconds, but hold on, it is working!

1238,2700,Cen Junda,Cen,Junda,59,M,Healthcare,Pharmaceuticals,,China,China,U,Cen Junda,Cen,China,Health Care,20978339,465,6851833323,0,0,-52426510,-0.76,Health Care,$6.85B,$0,-$52.4M,0%,-0.8%
1238,2700,Nik Storonsky,Storonsky,Nik,39,M,Finance & Investments,Fintech,,United Kingdom,United Kingdom,D,Nik Storonsky,Storonsky,United Kingdom,Finance,15275879,345,8629790000,0,0,25000000,0.29,Finance,$8.63B,$0,+$25.0M,0%,+0.3%
1380,2400,Geoffrey Kwok,Kwok,Geoffrey,38,M,Real Estate,Real estate,,Hong Kong,Hong Kong,D,Geoffrey Kwok,Kwok,Hong Kong,Real Estate,20900694,473,6738372594,0,0,-169487316,-2.45,Real Estate,$6.74B,$0,-$169M,0%,-2.5%
1496,2200,Adam Foroughi,Foroughi,Adam,43,M,Media & Entertainment,mobile games,,United States,United States,R,Adam Foroughi,Foroughi,United States,Technology,17870281,179,13664490528,-30915781,-0.26,1552493680,12.82,Technology,$13.7B,-$30.9M,+$1.55B,-0.3%,+12.8%
1545,2100,Gordon Getty,Getty,Gordon,90,M,Energy,Getty Oil,Ann & Gordon Getty Foundation,United States,United States,E,Gordon Getty,Getty,United States,Diversified,1654769,457,6950000000,0,0,200000000,2.96,Diversified,$6.95B,$0,+$200M,0%,+3.0%
1764,1800,Thomas Kwok,Kwok,Thomas,72,M,Real Estate,Real estate,,Hong Kong,Hong Kong,D,Thomas Kwok,Kwok,Hong Kong,Real Estate,1439938,227,11655118462,0,0,-159249666,-1.35,Real Estate,$11.7B,$0,-$159M,0%,-1.4%
1764,1800,Wang Ning,Wang,Ning,37,M,Media & Entertainment,Toys,,China,China,U,Wang Ning,Wang,China,Consumer,22082518,377,7977660369,-25000000,-0.33,339046896,4.44,Consumer,$7.98B,-$25.0M,+$339M,-0.3%,+4.4%
2046,1500,Torstein Hagen,Hagen,Torstein,81,M,Service,Cruises,,Switzerland,Norway,U,Torstein Hagen,Hagen,Norway,Services,16040629,208,12381281085,772487318,7.58,2184937274,21.43,Services,$12.4B,+$772M,+$2.18B,+7.6%,+21.4%
2410,1200,Raymond Kwok,Kwok,Raymond,70,M,Real Estate,Real estate,,Hong Kong,Hong Kong,D,Raymond Kwok,Kwok,Hong Kong,Real Estate,1534433,217,12202401519,0,0,31422257,0.26,Real Estate,$12.2B,$0,+$31.4M,0%,+0.3%
You should see a long list of names printed out in duplicate each time -- one is from one file, the other from the other file.
Great! But it would be nicer if these were in a file.
You also might want to not have every column from both files in your output data – we’ll look at how to do that later, too.
But before we learn how to do that, we’re going to take a little diversion to look at some command line jargon.


$ csvmatch \
forbes-billionaires.csv \
bloomberg-billionaires.csv \
--fields1 personName \
--fields2 commonName


This was the command we just ran.


$ csvmatch \
forbes-billionaires.csv \
bloomberg-billionaires.csv \
--fields1 personName \
--fields2 commonName


flags
arguments
We just gave CSV Match four bits of information:
The first two, the filenames, are called arguments – which means they are required.
The second two, with the dashes, are called flags – and are optional.
Flags can normally can be written two ways, the full way which is what’s here, where the flags start with two dashes, then a long description of what information you’re giving it.


$ csvmatch \
forbes-billionaires.csv \
bloomberg-billionaires.csv \
-1 personName \
-2 commonName


Most flags can be written in a short way, like here. This does the exact same thing.
Notice that they only start with a single dash.


$ csvmatch \
forbes-billionaires.csv \
bloomberg-billionaires.csv \
--fields1 personName \
--fields2 commonName \
> billionaires-in-both.csv

So let’s go back to the command we just ran.
Let’s look at how to put this data into a file.
You probably don’t want to type this in again, so just press the up key on your keyboard and it’ll come back.
To send the output from CSV Match into a file we need to add an angle bracket and then the name of our output file.
Try running that.
We should see a nice progress bar running across giving us some sense of how long this is going to take -- useful for bigger matches.
It’ll also tell you that there is a column called ‘rank’ in both files which it has disambiguated (ie. renamed) so it’s clear which file that column came from.
Then open the output file in Excel.
Once you’ve done that please shout out how many results you’re seeing!

You should see 377 rows.


Fuzzier matches with
normalisation
Now we’re at the fuzzy part.
So far when we’ve been talking about exact matches, I do mean exact – case-sensitive, in fact.
Though we can ignore case, we can also ignore a bunch of other things which might be incidental to a name.
This process of ignoring things can be thought of as normalisation.


What could we ignore?
Case (upper/lower)
Non-alphanumerics
Non-latin characters (é, å, ß, etc)
Words preceding the last
Words succeeding the first
The order the words are in
Common name prefixes (Mr, Ms, etc)
Terms specific to the data
These are some of the things we might want to ignore.


What could we ignore?
Case (upper/lower)
Non-alphanumerics
Non-latin characters (é, å, ß, etc)
Words preceding the last
Words succeeding the first
The order the words are in
Common name prefixes (Mr, Ms, etc)
Terms specific to the data
--ignore case
--ignore nonalpha
--ignore nonlatin
--ignore words-leading
--ignore words-tailing
--ignore words-order
--ignore titles
--ignore regex=EXPRESSION
CSV Match has the ignore flag which allows you to specify which of these characteristics should be disregarded.


What could we ignore?
Case (upper/lower)
Non-alphanumerics
Non-latin characters (é, å, ß, etc)
Words preceding the last
Words succeeding the first
The order the words are in
Common name prefixes (Mr, Ms, etc)
Terms specific to the data
-i case
-i nonalpha
-i nonlatin
-i words-leading
-i words-tailing
-i words-order
-i titles
-i regex=EXPRESSION
This also has a short format which means we don’t have to type as much.


Which world leaders went to Davos?
So let’s see how this works in practice.
Let’s find out how many names on the CIA’s world leaders list are also on the Davos participants list.


Let’s open up our CIA world leaders data in Excel.


There’s two important things here.
Firstly, the column name -- it’s just ‘name’.
The second, if we look at the names, we see they use the style of putting surnames in all-capitals. Also note that some names are surname-first.


Let’s also have a look at the Davos participants list.


Here’s our name column -- key thing is the column header, it’s just ‘name’ again.


$ csvmatch \
cia-world-leaders.csv \
davos-participants.csv \
--fields1 name \
--fields2 name


Let’s try a straight match, and see if we get any results.
Oh no, there aren’t any!


$ csvmatch \
cia-world-leaders.csv \
davos-participants.csv \
--fields1 name \
--fields2 name \
--ignore case \
> leaders-at-davos.csv

We saw that surnames were written in all-capitals in the world leaders list, but not in the Davos participants list, so that’s probably the reason.
Let’s try making our match case-insensitive, and we’ll put the output into a file too whilst we’re here.
If you don’t want to type everything out again, try pressing up on your keyboard in the terminal. It will show you the last command you ran, although it’ll all be on one line.
You can then add these bits to the bottom.
This will take a moment to run again.

You should have 74 rows.


Fuzzy matching with
multi-normalisation
Let’s take this one step further.


Orbán, Viktor

Viktor Orban
Let’s see how ignoring multiple things can give us a match.
These two names don’t match.
As far as a computer is concerned, they are totally different.


Orban, Viktor

Viktor Orban
Ignore non-latin characters.


Orban Viktor

Viktor Orban
Ignore non-alphanumerics.


Orban Viktor
=
Orban Viktor
Ignore word order.
And it’s a match!


Which world leaders went to COP?
Let’s try using that approach to answer a similar question.
Instead of Davos, let’s look at another dataset, the COP parties data.
This is our largest file at 14,000 rows, but you’ll see the match is still almost instant.


What could we ignore?
Case (upper/lower)
Non-alphanumerics
Non-latin characters (é, å, ß, etc)
Words preceding the last
Words succeeding the first
The order the words are in
Common name prefixes (Mr, Ms, etc)
Terms specific to the data
--ignore case
--ignore nonalpha
--ignore nonlatin
--ignore words-leading
--ignore words-tailing
--ignore words-order
--ignore titles
--ignore regex=EXPRESSION
If we look back at our slide from earlier, these are the five characteristics we’re going to ignore.


$ csvmatch \
cia-world-leaders.csv \
cop29-parties.csv \
--fields1 name \
--fields2 PartyName \
-i case nonalpha nonlatin words-order titles \
> leaders-at-cop.csv

I won’t run through opening COP parties data to look for the header.
Also note I’ve used the short form of the ignore flag – just a single dash.
It’s worth looking at the results, you can see how fuzzy we’ve made the match.

You should get 100 rows.


Fuzzy matching with
edit distances
That’s taken care of the basics, let’s look at a proper algorithm for doing this.
One approach is to simply look at how many characters are different – this is called the edit distance.


What is the edit distance?
Max Harlow  =  John Dales
90%
10%
Max Harlow  =  Max Harkow
This simply counts how many additions, removals, and substitutions needed to change one bit of text into another, giving a difference score at the end.
Then you have a threshold, and you decide that anything over that threshold is a match.
In CSV Match the default threshold is 60%, though you can change that as we’ll see later.


‘Levenshtein’
There are a few ways of doing this.
One of the most well-known methods is named Levenshtein, after a Russian mathematician who invented it.


Which billionaires went to Davos?
Let’s try and answer this question using the Forbes billionaires list.


$ csvmatch \
forbes-billionaires.csv \
davos-participants.csv \
--fields1 personName \
--fields2 name \
--method levenshtein \
> billionaires-at-davos.csv

This method is a bit slower than the normalisation approach we used previously.
The progress bar is also a bit misleading, it goes to 50% quickly then takes much longer to get to 100%.

You should have 2,250 rows.

But as you look through the data, you might see two matches and think -- those aren’t the same people at all!
There are some good matches here, but we can tell just by looking at others that they’re not going to be the same people.
This are mostly people with long forenames that match and short surnames that don’t.
Our powerful human brains understand that a surname match is more meaningful than a forename match, but this matching method doesn’t.
This might be fine for for matching company names, but for human names we have a problem.
We could improve the quality of these matches by splitting out first names from second names.
There is actually a more general thing going on here though.


False positives
& false negatives
So these are errors, but there are actually two different types of errors.
The first type are the ones we see in our data -- false positives, where the computer thinks two things are the same when they actually aren’t.
The other type are the records that we don’t see in our data -- false negatives, where the computer thinks two things aren’t the same, when they really are.


FALSE POSITIVE
FALSE NEGATIVE
this is coffee
this is not coffee
Here’s a real life example.
On the left, a false positive.
On the right, what appears to be a false negative.
The amount of false positives can also be called precision, the amount of false negatives is recall.
In our data, it’s a tradeoff between having more of one or the other.
On projects like those I’ve described, we probably want to bias towards having more false positives -- as we’re going to manually go through the results anyway.
And we can’t go through results that aren’t there.
Of course you don’t want too much manual work.
By default CSV Match is set to needing 60% of the characters being the same for it to be a match.


Seeing the strength
of a match
So by default CSV Match outputs every column from the first file followed by every column from the second.
However we can specify exactly which columns we want to appear in the output.
This is not about which columns are used for matching, it’s purely about the output.
We can also use this to add a column that will show us how closely two names match.


$ csvmatch \
forbes-billionaires.csv \
davos-participants.csv \
--fields1 personName \
--fields2 name \
--method levenshtein \
--output 1.personName 2.name degree \
> billionaires-at-davos-with-degree.csv
So let’s go back to our command.
We are now going to add this output line to tell it which columns we want in the output.
Don’t type this out now, let’s first look at the new line in more detail.


--output 1.personName 2.name degree \


--output 1.personName 2.name degree \

Firstly we are giving it the output flag -- this is a flag that lets us specify which exact columns we want in our output.


--output 1.personName 2.name degree \

Then there are three column specifications afterwards, separated by spaces.
So our output will have three columns.


--output 1.personName 2.name degree \

These column specifications start with the number of the file that the column is in.
I’ve taken the name column from the first file, which in the Forbes file is called personName.
So we have a number one, then there’s a dot.
Then there’s the name of the column as it is in that file.


--output 1.personName 2.name degree \

We then bring in the name column from the second file, the Davos file.


--output 1.personName 2.name degree \

And our third column we want in the output is the degree to which the two match.
This is a special column that doesn’t come from either file so it doesn’t have a number before it.


$ csvmatch \
forbes-billionaires.csv \
davos-participants.csv \
--fields1 personName \
--fields2 name \
--method levenshtein \
--output 1.personName 2.name degree \
> billionaires-at-davos-with-degree.csv
no need to type this out!
go here: bit.ly/nicar25-fuzzy-commands
If you don’t want to type all that out you can go to this Bitly link which has all the commands we’ve run today, scroll to the second to last one and copy paste it into the terminal.
Now try running this yourself, and check out the output.
So the results are the same as before, but now we can see exactly how much better some matches are than others.


Advanced fuzzy matching with
blocking
Now let’s look at how we can actually improve matches like this – by using multiple fields.
This is the most powerful technique we’re going to see today.
That’s because it can make your matches both more accurate and faster.


Here’s the Forbes billionaires file again.
You might not have noticed before, but on the far right there’s a country column.


And this is the Davos participants file – we also have a country column, with the same name.
This is often the case when we’re matching two datasets – there are other columns with relevant information.
In this case, country of residence, but it could also be states or dates of birth.
We can use this information in our match.
This can make matching more accurate.
If we have two people with the same name but we know one lives in Australia and the other lives in the UK, they shouldn’t be a match.
Using this data can also, perhaps counterintuitively, make matches faster too!
The data files we’ve been using today have been fairly small, so it hasn’t mattered so much.
But with bigger files this starts to become important.
Let’s see how.


file 1
file 2
rows
rows
Let’s say we have two files, both with 100 rows with names of people.
What’s the most possible matches we could have?


file 1
file 2
10,000
comparisons
rows
rows
The answer is 10,000 – it’s 100 x 100.
So the computer has to make that many comparisons in order to produce a result.


rows

file 1
file 2
rows

rows

rows

But let’s say half of the names in this file were people who live in the UK and the other half are in the US.
And we never want names of people living in the UK to match with names of people living in the US.
We still have the same number of rows overall.


file 1
file 2
2,500
 
2,500
comparisons
rows

rows

rows

rows

If we do 50 multiplied by 50 we get 2,500 for the UK names, then the same again for the US names.
So we’re only matching UK names with UK names and US names with US names – so it should be more accurate.
That means the computer did 2,500 comparisons for each.


file 1
file 2
5,000
comparisons
rows

rows

rows

rows

And that’s 5,000 overall.
That’s half the number of comparisons the computer has to do – so this could potentially take half the time.
Plus it’s likely to be more accurate as we are only matching names within countries!
This is the idea of blocking.


Which billionaires went to Davos?
Let’s try answering this question again using blocking.


$ csvmatch \
forbes-billionaires.csv \
davos-participants.csv \
--fields1 country \
--fields1 personName \
--fields2 country \
--fields2 name \
--method literal levenshtein \
--threshold 0.8 \
> billionaires-at-davos-2.csv
no need to type this out!
go here: bit.ly/nicar25-fuzzy-commands
Ok this is our last command, and the longest.
Again, feel free to copy and paste this.

Let’s look at the bits that are new:
We are specifying the fields1 and fields2 flags twice! The first time to give the country columns, our first block, and the second time for the name columns.
The method flag has two methods listed – it first says ‘literal’ as the first block of country codes should be matched exactly, and then levenshtein for the second block with the names.
Lastly I’m also adding a new flag, threshold – this lets us set the degree so there Levenshtein requires an 80% match.
When you run this you will see two progress bars, one for each block.

You should get 47 matches.


$ csvmatch \
forbes-billionaires.csv \
davos-participants.csv \
--fields1 country \
--fields1 personName \
--fields2 country \
--fields2 name \
--method literal levenshtein \
--threshold 0.8 \
> billionaires-at-davos-2.csv
To make this clearer I’ve highlighted which parts of that command refer to which block.
So for every block we need to give it at least three bits of information – the two column names and the matching method.
The first block based on countries and literal matching is highlighted red.
The second block based on names and Levenshtein matching is highlighted blue.
The threshold is a special case, technically it applies to both, although literal matches are always zero or one so it makes no difference for the first block.


Other matching methods
We’ve covered a couple of methods here, but there are others that CSV Match supports which we don’t have time to play with.


phonetics!
machine learning!
One uses the phonetics of how names are typically pronounced in English.
It works well where you have names that have typos or have been transcribed from being heard verbally, such as from a telephone call, or when you have names written in another language that have been transliterated into English.
Another method uses machine learning.
In this one you have to train the algorithm – it starts asking you whether different pairs are the same, and once you’ve given it enough information it extrapolates out what you’ve taught it over your entire datasets.

AI is getting better every day, and it's worth considering. But you don't know what it's really doing. It is also non-deterministic, and it can be slow and expensive. So it might be worth trying, and even more so in the future, but I would still recommend you start with the approaches I've discussed here


Know your data
We’re now at the end of this session, but before you leave there’s a couple of things I think you need to keep in mind when doing fuzzy matching.
A lot depends on the nature of your specific data, what kind of issues it has and how it was produced can guide your approach.
For example, the donations data I showed you at the start – this used to include lots of people with ‘na’ in their name – this is how names were entered for people with no middle name, by putting ‘not applicable’ in that field in a form.
Knowing these kinds of details let you tackle them – removing something like this could be achieved with a custom normalisation.
That all said fuzzy matching itself can be a bit of a fuzzy science, and it’s often worthwhile to try a few different approaches and see what works best.


Same name, same person
Keep in the back of your mind when matching up records like this that two people or two companies with the same name aren’t necessarily the same!
Even if it’s an exact match.


Textmatch
github.com/maxharlow/textmatch
We’ve been using CSV Match today which runs on the command line, but if you know Python, or are learning it, you may prefer to use it that way, which is possible!
Textmatch has a very similar interface to CSV Match, but works as a Python library instead of on the command line.
CSV Match actually uses this internally to do the matching.
This Github link has documentation on how to use it.
There are also various other libraries for doing fuzzy matching, which are linked to at the end of the Textmatch readme file.


@maxharlow.bsky.social
github.com/maxharlow/csvmatch
bit.ly/nicar25-fuzzy



## What changes are “in scope”

Common, safe changes:

- Fix typos and broken links in `docs/`.
- Update or correct workflow YAML examples in `.github/workflows/`.
- Update the Observable app in `site/` (content, build config, small UX improvements).
- Refresh documentation build/deploy automation.

Changes to avoid unless explicitly requested:

- Large refactors of the tutorial structure or tone.
- Renaming workflow files or chapter filenames (links/bookmarks may break).
- Introducing new heavy dependencies.


## Project layout

- `docs/`: Sphinx + MyST markdown documentation.
  - Primary entry point: `docs/index.md`
  - Sphinx config: `docs/conf.py`
  - Build output (local): `docs/_build/`
- `.github/workflows/`: Example Actions workflows used by the tutorial.
  - Docs build/deploy: `.github/workflows/docs.yaml`
  - Scrape + Pages deploy: `.github/workflows/scrape-and-deploy.yaml`
  - Matrix scraping example: `.github/workflows/scraper-with-matrix.yaml`
  - EC2 runner examples: `.github/workflows/reusable-ec2-job.yaml`, `.github/workflows/ec2-custom-runner.yaml`
- `site/`: Observable Framework app used for the dashboard deployment chapter.
  - Config: `site/observablehq.config.js`
  - Source: `site/src/` (Markdown pages + data loaders/static data)
  - Build output: `site/dist/` (generated)
- `data/`: Scraper outputs committed by workflows (CSV files).



## Skills

This repo includes reusable skills in the `skills/` directory that agents can use to accomplish tasks more efficiently.

### Browser Screenshots (`skills/browser-screenshots/`)

Use this skill to capture screenshots for the tutorial documentation. Screenshots are stored in `docs/_static/` and can be embedded in the Sphinx documentation.

**Installation (one-time):**

```bash
npm install playwright
npx playwright install chromium
```

**Common use cases for this project:**

```bash
# Capture GitHub Actions pages for tutorials
node skills/browser-screenshots/scripts/capture.cjs \
  --url https://github.com/palewire/go-big-with-github-actions/actions \
  --output docs/_static/actions-homepage.png

# Capture workflow runs with highlighting
node skills/browser-screenshots/scripts/capture.cjs \
  --url https://github.com/palewire/go-big-with-github-actions/actions/workflows/scrape-and-deploy.yaml \
  --highlight ".workflow-run-status" \
  --output docs/_static/workflow-status.png

# Capture GitHub Pages settings
node skills/browser-screenshots/scripts/capture.cjs \
  --url https://github.com/palewire/go-big-with-github-actions/settings/pages \
  --output docs/_static/pages-settings.png

# Capture local Observable dashboard during development
node skills/browser-screenshots/scripts/capture.cjs \
  --url http://localhost:3000 \
  --output docs/_static/dashboard-preview.png
```

**Embedding in docs:**

After capturing, embed in MyST markdown:

```markdown
```

See `skills/browser-screenshots/SKILL.md` for full documentation including options for dark mode, full-page captures, element selection, and JavaScript execution.


## Tooling

### Python (docs)

- Python requirement: **3.12** (see `pyproject.toml`).
- Dependency manager: **uv** (see `uv.lock`).
- Docs stack: Sphinx + MyST.

### JavaScript (dashboard)

- Node requirement: `>=18` (the workflows use Node **20.11**).
- Package manager: npm (see `site/package.json`).

### Formatting / linting

This repo uses `pre-commit` with:

- `ruff` + `ruff-format`
- `mypy`
- `blacken-docs` (formats Python snippets inside docs)
- standard whitespace/yaml/json checks



## Common commands

Run these from the repository root unless stated otherwise.

### Install (docs)

- Install Python deps using uv:
  - `uv sync`

### Live docs server

- Start live-reloading docs server (clears build output first):
  - `make serve`

This runs the Sphinx autobuild server (typically http://localhost:8000).

### Build docs (one-off)

- Build HTML docs:
  - `uv run sphinx-build -M html ./docs ./_build/`

### Lint/format (recommended via pre-commit)

- Run all configured checks:
  - `uv run pre-commit run --all-files`

If you are making doc changes, ensure `check-yaml`, `ruff-format`, and `blacken-docs` pass.

### Observable dashboard (site)

- Install deps:
  - `npm install --prefix site`
- Local preview server:
  - `npm run dev --prefix site`
- Build static output:
  - `npm run build --prefix site`


## CI / automation notes

### Docs pipeline

- `.github/workflows/docs.yaml` builds Sphinx docs using `uv sync` and uploads artifacts.
- On `main`, it deploys to S3 using `datadesk/delivery-deploy-action@v1`.
- Deployment requires AWS secrets (`DOCS_AWS_*`) configured in the GitHub repo settings.

### Scrape + deploy pipeline

- `.github/workflows/scrape-and-deploy.yaml`:
  - Scrapes Iowa WARN data using `warn-scraper` and commits results into `data/`.
  - Builds the Observable site and deploys it to GitHub Pages.

When editing this workflow, keep in mind:

- It uses `permissions: contents: write` to allow committing scraped data.
- Pages deploy uses `actions/upload-pages-artifact` + `actions/deploy-pages`.

### Matrix scraping example

- `.github/workflows/scraper-with-matrix.yaml` demonstrates:
  - `strategy.matrix` to run multiple scrapes in parallel.
  - Artifact fan-in and a follow-up commit job.

### EC2 runner example

- `.github/workflows/reusable-ec2-job.yaml` provisions an ephemeral self-hosted runner on AWS EC2 via `machulav/ec2-github-runner@v2`.
- `.github/workflows/ec2-custom-runner.yaml` calls the reusable workflow.

These workflows are tutorial examples; treat them as reference code and be cautious about changing default regions/AMI IDs/instance types without a specific request.



## Conventions for agents

- Prefer minimal diffs that preserve the tutorial’s intent.
- Keep workflow examples readable: clear step names, consistent quoting, and stable action versions.
- Avoid changing public URLs and file names referenced by the docs unless you also update links and navigation.
- Do not commit generated build artifacts such as `docs/_build/` or `site/dist/`.
- If you adjust dependencies:
  - For Python: update `pyproject.toml` and regenerate `uv.lock` (via `uv sync`).
  - For Node: update `site/package.json` and `site/package-lock.json` if present.


## Quick “sanity check” before opening a PR

- `uv run pre-commit run --all-files`
- `make serve` (ensure docs build locally)
- If you touched `site/`: `npm run build --prefix site`



## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.


## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
 advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
 address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
 professional setting



## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.


## Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.



## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at datadesk@latimes.com. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.


## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
https://www.contributor-covenant.org/faq



## Installation

Fork the repository and clone it:

```bash
gh repo clone your-name/go-big-with-github-actions
```

Change into the project directory:

```bash
cd go-big-with-github-actions
```

Install the dependencies using uv:

```bash
uv install
```


## Contributing

To start a test server the previews the site, use the following command:

```bash
make serve
```

Once it starts, visit [localhost:8000](http://localhost:8000) in your browser. Edits made in the `docs/` folder will appear immediately. Commit your changes to a branch and then submit a pull request to the source repository.



## Reporting a Vulnerability

If you have found a vulnerability in this project, please contact maintainer Ben Welsh at [b@palewi.re](mailto:b@palewi.re)


## Get started on GitHub

If you already have a GitHub account, please log in. If you do not have one, please create one on [github.com](https://github.com) and use it to log in to the site.

Once you are logged into GitHub, create a new repository by clicking on the "New" button at the top-left corner or simply click this link: [github.com/new](https://github.com/new).

Now, fill in a name for your new repository. A good example would be `go-big-with-github-actions`. Make sure your repository is public, which will allow us to access an important feature later in the class.


Click on the "Create repository" button at the bottom of the form.




## Create a simple Action

Navigate to your repository's homepage in the browser. Click on the "Actions" tab, which will take you to a page where you can create, manage and monitor your Actions.


Scroll down the page. You will see that GitHub offers a menu of templates for common automation tasks. For our first Action, we will click "set up a workflow yourself" link near the top of the page.

:::{admonition} Note
The terms action, workflow, job and task and yaml are often used interchangeably by GitHub Actions users to refer to these configuration files.


This will open up an editor inside of your browser, which is another one of the features offered by GitHub.

Let's start by renaming the file to `simple.yaml` in the box above the editor. This will be the name of your first Action file.


:::{admonition} Note
We will be editing our files inside of GitHub using our browser in this manner throughout the tutorial. If you're already a GitHub expert and you'd prefer to clone your repo and use a code editor instead, please feel free to do so. Just make sure to push your changes back to GitHub as you go.


## Start your workflow

First, we will name our Action by adding the following line at the top of the file.

```yaml
name: First Action
```

You will notice a red squiggly underline beneath your code. This means that GitHub sees something wrong with your workflow. When you hover over the squiggly line, a hint will appear. Here we see it says "Missing required root key `on`."

Let's take the hint and add another line under `name`.

```yaml
on:
  workflow_dispatch:
```

They keyword `on` is used to determine when the Action file will run. When it is configured with `workflow_dispatch`, the Action can be run manually from the monitoring panel.

:::{admonition} Note
You can read more about different options for configuring `on` [in GitHub's documentation](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#on).

Now let's tell our workflow what we want it to do.

Copy and paste the below code under `workflow_dispatch:`.

```yaml
jobs:
  hello:
    name: Say Hello
    runs-on: ubuntu-latest
    steps:
      name: Hello world
      run: echo "Hello world"
```

Be mindful of indentation and uneven syntax. The red squiggly marks will give you hints if there's anything wrong with your file.

Your workflow file should now look something like this:

```yaml
name: First Action

on:
  workflow_dispatch:

jobs:
  hello:
    name: Say Hello
    runs-on: ubuntu-latest
    steps:
      - name: Hello world
        run: echo "Hello world"
```

A workflow run consists of one or more `jobs`, which can run sequentially or in parallel depending on your configuration. In this simple case we only have a single job called `hello`.

{emphasize-lines="6-7"}
```yaml
name: First Action

on:
  workflow_dispatch:

jobs:
  hello:
    name: Say Hello
    runs-on: ubuntu-latest
    steps:
      - name: Hello world
        run: echo "Hello world"
```

For each job, you will need to choose what kind of server to use. In our case, we selected an Ubuntu Linux runner. You can also choose MacOS or Windows.

{emphasize-lines="9"}
```yaml
name: First Action

on:
  workflow_dispatch:

jobs:
  hello:
    name: Say Hello
    runs-on: ubuntu-latest
    steps:
      - name: Hello world
        run: echo "Hello world"
```

Each job then runs as many `steps` as you want to layout as a list. Give each task a name and tell it what to do. In our case, we are simply printing out "Hello world" to the console using the built-in [`echo`](https://linux.die.net/man/1/echo) command.

{emphasize-lines="10-12"}
```yaml
name: First Action

on:
  workflow_dispatch:

jobs:
  hello:
    name: Say Hello
    runs-on: ubuntu-latest
    steps:
      - name: Hello world
        run: echo "Hello world"
```


Now save your file to the repository by clicking on the green "Commit changes" button in the top-right corner.


In GitHub, all workflow files are saved under `.github > workflows` folder. Your first commit has created the folder and saved your first workflow for you. When you are ready to add more workflows, you should add them to this folder as well.


If you need to edit this first file again, simply click into the file and click the pencil icon on the top right corner.




## Run your action

Go back to your "Actions" tab in the repository. You will see that your workflow is now available in the left rail. Click on its name there. Then go to the right corner where you will see a dropdown called "Run workflow." Click the second, green "Run workflow" button it presents in a dropdown to kickstart your first job.


Refresh your browser. Once your Action has been completed, you will see a green checkmark to the left. Clicking on the completed action will show you what job just ran. Click on the job and open up the steps within workflow to see the output.



## What you will learn

Work through this tutorial and you will gain hands-on experience creating automated systems that can collect, process and publish gigantic datasets with ease.

It will teach you how to:

* Schedule an automated task
* Scrape and store data from a newsworthy source
* Scale up to run hundreds of tasks in parallel
* Publish a data dashboard to share your work
* Extend GitHub’s free system to access mammoth amounts of computing power



## Who can take it

This course is free. Previous experience working with GitHub will be useful, but anyone with a good attitude is qualified to take the class.


## Table of contents

```{toctree}
:maxdepth: 1
:name: mastertoc
:numbered:

what-are-actions
what-is-yaml
getting-started
scraper
matrix
deploy
ec2
```



## About this class

[Ben Welsh](https://palewi.re/who-is-ben-welsh/), [Iris Lee](https://www.irisslee.com/) and [Dana Chiueh](https://dana.computer/) prepared this guide for [a training session](https://schedules.ire.org/nicar-2025/index.html#2045) at the National Institute for Computer-Assisted Reporting’s 2025 conference in Minneapolis. GitHub’s Copilot, an AI-powered text generator, provided some assistance. The materials are available as free and [open source on GitHub](https://github.com/palewire/go-big-with-github-actions).


## Matrix strategy

Take a look at the scraping logic we implemented earlier. Under the scrape job, we will define the matrix strategy. Here, we'd like to provide a list of states to scrape.

{emphasize-lines="13-15"}
```yaml
name: Matrix Scraper

on:
  workflow_dispatch:

permissions:
  contents: write

jobs:
  scrape:
    name: Scrape
    runs-on: ubuntu-latest
    strategy:
      matrix:
        state: [ca, ia, ny]
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Install Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.12'

      - name: Install scraper
        run: pip install warn-scraper

      - name: Scrape
        run: warn-scraper ${{ inputs.state }} --data-dir ./data/

      - name: Save datestamp
        run: echo "Scraped ${{ inputs.state }}" > ./data/latest-scrape.txt

      - name: Commit and push
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@users.noreply.github.com"
          git add ./data/
          git commit -m "Latest data for ${{ inputs.state }}" && git push || true
```

In our original scraper, we combined scraping and committing in a single step because we weren't worried about first pulling the latest repo changes. However, with multiple jobs running in parallel, we can no longer guarantee their order of completion. In this chapter, we'll solve that by splitting the action into two steps.

First, we'll run all scrapers in parallel and save their outputs in temporary storage known as artifacts.

Then, once every job finishes, we'll collect those Artifacts and make a single commit. This approach ensures that all parallel jobs contribute their changes without overwriting each other.

### Error handling

GitHub Actions provides two error-handling settings that will be helpful. One is called ```fail-fast```. This flag controls whether the entire matrix job should fail if one job in the matrix fails. In our case, we want to mark this flag as false; even if one state's scraper fails, we still want the job to be completed and continue scraping the other states.

{emphasize-lines="7"}
```yaml
jobs:
  scrape:
    name: Scrape
    runs-on: ubuntu-latest
    continue-on-error: true
    strategy:
      fail-fast: false
      matrix:
        state: [ca, ia, ny]

```

The second error-handling setting is called `continue-on-error.` When true, this allows the Action to continue running subsequent steps even if an earlier step fails. Since our Action has multiple jobs—a build job and a commit job—we want the Action to continue running even if one of the scrapes fails earlier.

{emphasize-lines="5"}
```yaml
jobs:
  scrape:
    name: Scrape
    runs-on: ubuntu-latest
    continue-on-error: true
    strategy:
      fail-fast: false
      matrix:
        state: [ca, ia, ny]

```

To accommodate our matrix strategy, we'll also modify all the steps that use the `inputs.state` variable to use `matrix.state` instead. For example, in the "Scrape" step, we change the line to:

{emphasize-lines="2"}
```yaml
      - name: Scrape
        run: warn-scraper ${{ matrix.state }} --data-dir ./data/
```

We should do the same for the scraping step. For simplicity, let's remove that datestamp step for now.

```yaml
name: Matrix Scraper

on:
  workflow_dispatch:

permissions:
  contents: write

jobs:
  scrape:
    name: Scrape
    runs-on: ubuntu-latest
    continue-on-error: true
    strategy:
      fail-fast: false
      matrix:
        state: [ca, ia, ny]
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Install Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.12'

      - name: Install scraper
        run: pip install warn-scraper

      - name: Scrape
        run: warn-scraper ${{ matrix.state }} --data-dir ./data/
```



## Uploading artifact

Now that we've scraped our data, we need a place to store it before we commit it to the repo. To do this, we are using Actions Artifacts. Artifacts allow you to persist data after a job has completed and share that data with another job in the same workflow. An artifact is a file or collection of files produced during a workflow run.

Here, we are using the shortcut [actions/upload-artifact](https://github.com/actions/upload-artifact) created by GitHub, which allows us to temporarily store our data within our task.

{emphasize-lines="33-37"}
```yaml
name: Matrix Scraper

on:
  workflow_dispatch:

permissions:
  contents: write

jobs:
  scrape:
    name: Scrape
    runs-on: ubuntu-latest
    continue-on-error: true
    strategy:
      fail-fast: false
      matrix:
        state: [ca, ia, ny]
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Install Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.12'

      - name: Install scraper
        run: pip install warn-scraper

      - name: Scrape
        run: warn-scraper ${{ matrix.state }} --data-dir ./data/

      - name: upload-artifact
        uses: actions/upload-artifact@v6
        with:
          name: ${{ matrix.state }}
          path: ./data/${{ matrix.state }}.csv
```


## Commit step

Next, let's create a second step for our Action: the commit step. We'll start with the standard step of checking out the code. Notice that the step needs the scraping step, which ensures it will not run until our first step has finished.

{emphasize-lines="4"}

```yaml
  commit:
      name: Commit
      runs-on: ubuntu-latest
      needs: scrape
      steps:
        - name: Checkout
          uses: actions/checkout@v6
```

The next step is to download the artifacts we previously stored for use in this step. This is done using the `actions/download-artifact` companion to the uploader.

{emphasize-lines="9-13"}

```yaml
  commit:
    name: Commit
    runs-on: ubuntu-latest
    needs: scrape
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Download artifact
        uses: actions/download-artifact@v7
        with:
          pattern: '*'
          path: artifacts/
```

To keep our repo clean, we can add a `Move` step to unpack the artifacts—which are all stored in their own folders since they came from different parallel jobs—and put them into our `data/` folder. Lastly, we push with the same code as before.

{emphasize-lines="15-18"}
```yaml
  commit:
    name: Commit
    runs-on: ubuntu-latest
    needs: scrape
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Download artifact
        uses: actions/download-artifact@v7
        with:
          pattern: '*'
          path: artifacts/

      - name: Move
        run: |
          mkdir data -p
          mv artifacts/**/*.csv data/
```

We can add a logging step here to save the current date and time to a file. This will help us track when the last scrape was done and prevent GitHub from deactivating the workflow.

{emphasize-lines="20-21"}
```yaml
  commit:
    name: Commit
    runs-on: ubuntu-latest
    needs: scrape
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Download artifact
        uses: actions/download-artifact@v7
        with:
          pattern: '*'
          path: artifacts/

      - name: Move
        run: |
          mkdir data -p
          mv artifacts/**/*.csv data/

      - name: Save datestamp
        run: date > ./data/latest-scrape.txt
```

Finally, we can add the same commit and push step as before. This time, we don't need to specify the state in the commit message since all states are now included in the data folder.

{emphasize-lines="23-28"}
```yaml
  commit:
    name: Commit
    runs-on: ubuntu-latest
    needs: scrape
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Download artifact
        uses: actions/download-artifact@v7
        with:
          pattern: '*'
          path: artifacts/

      - name: Move
        run: |
          mkdir data -p
          mv artifacts/**/*.csv data/

      - name: Save datestamp
        run: date > ./data/latest-scrape.txt

      - name: Commit and push
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@users.noreply.github.com"
          git add ./data/
          git commit -m "Latest data" && git push || true
```

All together, our final code should look like this:

```yaml
name: Matrix Scraper

on:
  workflow_dispatch:

permissions:
  contents: write

jobs:
  scrape:
    name: Scrape
    runs-on: ubuntu-latest
    continue-on-error: true
    strategy:
      fail-fast: false
      matrix:
        state: [ca, ia, ny]
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Install Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.12'

      - name: Install scraper
        run: pip install warn-scraper

      - name: Scrape
        run: warn-scraper ${{ matrix.state }} --data-dir ./data/

      - name: upload-artifact
        uses: actions/upload-artifact@v6
        with:
          name: ${{ matrix.state }}
          path: ./data/${{ matrix.state }}.csv

  commit:
    name: Commit
    runs-on: ubuntu-latest
    needs: scrape
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Download artifact
        uses: actions/download-artifact@v7
        with:
          pattern: '*'
          path: artifacts/

      - name: Move
        run: |
          mkdir data -p
          mv artifacts/**/*.csv data/

      - name: Save datestamp
        run: date > ./data/latest-scrape.txt

      - name: Commit and push
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@users.noreply.github.com"
          git add ./data/
          git commit -m "Latest data" && git push || true
```




## Breaking our action?

What happens when we try to scrape a state that doesn't exist in the scraper? For example, `mn` WARN notices are not supported by Big Local News' WARN Scraper. Let's try changing our list of scraped states:

{emphasize-lines="9"}
```yaml
jobs:
  scrape:
    name: Scrape
    runs-on: ubuntu-latest
    continue-on-error: true
    strategy:
      fail-fast: false
      matrix:
        state: [mn, md, tn, wv, ny]
```
Now, commit and rerun the action.


We can see that thanks to `fail-fast`, `mn` and `wv` fail (because the WARN scraper does not support these states), while `md`, `tn` and `ny` succeed. And thanks to `continue-on-error`, even though there were failures in the first scrape step, the action continued to run to the commit step and push the newly scraped data into the repo.


## Create a new workflow

Let's begin by starting a new workflow file. Go to your repository's homepage in the browser. Click on the "Actions" tab, which will take you to a page where you manage Actions. Now click on the "New workflow" button.


Click the "set up a workflow yourself" link again.


This time let's call this file `scraper.yml`.




## Write your workflow file

Start with a `name` and expand the `on` parameter we used last time by adding a `cron` setting. Here, we've added a crontab expression that will run the Action every day at 00:00 UTC.


{emphasize-lines="5-6"}
```yaml
name: First Scraper

on:
  workflow_dispatch:
  schedule:
  - cron: "0 0 * * *"
```

:::{admonition} Note
[Crons](https://en.wikipedia.org/wiki/Cron), sometimes known as crontabs or cron jobs, are a way to schedule tasks for particular dates and times. They are a powerful tool but a bit tricky to understand. If you need help writing a new pattern, try using [crontab.guru](https://crontab.guru/).

Next, add a simple job named `scrape`.

{emphasize-lines="8-12"}
```yaml
name: First Scraper

on:
  workflow_dispatch:
  schedule:
  - cron: "0 0 * * *"

jobs:
  scrape:
    name: Scrape
    runs-on: ubuntu-latest
    steps:
```

Think of Actions as renting a blank computer from GitHub. To use it, you will need to install the latest version of whatever language you are using, as well as any corresponding package managers and libraries.

Because these Actions are used so often, GitHub has a [marketplace](https://github.com/marketplace?type=actions) where you can find pre-packaged steps for common tasks.

The `checkout` action clones our repository onto the server so that all subsequent steps can access it. We will need to do this so that we can save the scraped data back into the repo at the end of the workflow.

{emphasize-lines="13-14"}
```yaml
name: First Scraper

on:
  workflow_dispatch:
  schedule:
  - cron: "0 0 * * *"

jobs:
  scrape:
    name: Scrape
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v6
```

Our scraper will gather the latest mass layoff notices posted on government websites according to the U.S. Worker Adjustment and Retraining Notification Act requirements, also known as the WARN Act. It's an open-source software package developed by [Big Local News](https://biglocalnews.org/content/tools/layoff-watch.html), which uses the Python computer programming language.

So our next step is to install Python, which can also be accomplished with a pre-packaged action.

{emphasize-lines="16-19"}
```yaml
name: First Scraper

on:
  workflow_dispatch:
  schedule:
  - cron: "0 0 * * *"

jobs:
  scrape:
    name: Scrape
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Install Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.12'
```

Now we will use Python's `pip` package manager to install the `warn-scraper` package.

{emphasize-lines="21-22"}
```yaml
name: First Scraper

on:
  workflow_dispatch:
  schedule:
  - cron: "0 0 * * *"

jobs:
  scrape:
    name: Scrape
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Install Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.12'

      - name: Install scraper
        run: pip install warn-scraper
```

According to the package's [documentation](https://warn-scraper.readthedocs.io/en/latest/usage.html), all we need to do to scrape a state's notices is to type `warn-scraper <state>` into the terminal.

Let's scrape Iowa, America's greatest state, and store the results in the `./data/` folder at the root of our repository.

{emphasize-lines="24-25"}
```yaml
name: First Scraper

on:
  workflow_dispatch:
  schedule:
  - cron: "0 0 * * *"

jobs:
  scrape:
    name: Scrape
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Install Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.12'

      - name: Install scraper
        run: pip install warn-scraper

      - name: Scrape
        run: warn-scraper ia --data-dir ./data/
```

Finally, we want to commit this scraped data to the repository and push it back to GitHub.

{emphasize-lines="30-35"}
```yaml
name: First Scraper

on:
  workflow_dispatch:
  schedule:
  - cron: "0 0 * * *"

jobs:
  scrape:
    name: Scrape
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Install Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.12'

      - name: Install scraper
        run: pip install warn-scraper

      - name: Scrape
        run: warn-scraper ia --data-dir ./data/

      - name: Commit and push
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@users.noreply.github.com"
          git add ./data/
          git commit -m "Latest data for Iowa" && git push || true
```

Save this workflow to our repo. Go to the `Actions` tab, choose your scraper workflow, and click `Run workflow`, as we did in the previous chapter.

Once the task has been completed, click its list item for a summary report. You will see that Action was unable to access the repository. This is because GitHub Actions requires that you provide [permissions](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#permissions).


Let's go ahead and add the line so that we can provide write permission to all jobs.

{emphasize-lines="8-9"}
```yaml
name: First Scraper

on:
  workflow_dispatch:
  schedule:
  - cron: "0 0 * * *"

permissions:
  contents: write

jobs:
  scrape:
    name: Scrape
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Install Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.12'

      - name: Install scraper
        run: pip install warn-scraper

      - name: Scrape
        run: warn-scraper ia --data-dir ./data/

      - name: Commit and push
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@users.noreply.github.com"
          git add ./data/
          git commit -m "Latest data for Iowa" && git push || true
```

Save the file and rerun the Action.

Once the workflow has been completed, you should see the `ia.csv` file in your repository's `data` folder.



## User-defined inputs

GitHub Actions allows you to specify `inputs` for manually triggered workflows, which we can enable users to specify what state to scrape.

To add an input option to your workflow, go to your YAML file and add the following lines. Here, we ask Actions to create an `input` called `state`. A given Action can have more than one input.

If you need more control over your inputs, you can also add [choices](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#onworkflow_dispatchinputs).

{emphasize-lines="4-9"}
```yaml
name: First Scraper

on:
  workflow_dispatch:
    inputs:
      state:
        description: 'U.S. state to scrape'
        required: true
        default: 'ia'
  schedule:
  - cron: "0 0 * * *"
```

Once your input field has been configured, let's change our warn-scraper command so that whatever we input as `state` will be reflected in the scrape command.

```yaml
      - name: Scrape
        run: warn-scraper ${{ inputs.state }} --data-dir ./data/
```

### Customize your commit message

You can add these inputs anywhere! Add them to your commit message for accuracy.

```yaml
      - name: Commit and push
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@users.noreply.github.com"
          git add ./data/
          git commit -m "Latest data for ${{ inputs.state }}" && git push || true
```
### Add a datestamp

GitHub may automatically [disable workflows](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/disabling-and-enabling-a-workflow) if there's a period of inactivity.
To get around this you can have your workflow commit an updated text file every time your Action runs.

```yaml
      - name: Save datestamp
        run: date > ./data/latest-scrape.txt
```



## Final steps

Your final file should look like this.

```yaml
name: First Scraper

on:
  workflow_dispatch:
    inputs:
      state:
        description: 'U.S. state to scrape'
        required: true
        default: 'ia'
  schedule:
  - cron: "0 0 * * *"

permissions:
  contents: write

jobs:
  scrape:
    name: Scrape
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Install Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.12'

      - name: Install scraper
        run: pip install warn-scraper

      - name: Scrape
        run: warn-scraper ${{ inputs.state }} --data-dir ./data/

      - name: Save datestamp
        run: date > ./data/latest-scrape.txt

      - name: Commit and push
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@users.noreply.github.com"
          git add ./data/
          git commit -m "Latest data for ${{ inputs.state }}" && git push || true
```

Let's rerun the Action. Now when you go to run your Action, you will see an input field. This will allow you to specify which state to scrape for. Here I'm choosing CA.


Upon completion, you will see that steps that reference `inputs.state` have been run with the correct value.


You are not limited to third-party packages like `warn-scraper`. You can run any script you include in your repository.

If you'd like an example to try out, check out the [scrape.ipynb](https://github.com/palewire/go-big-with-github-actions/blob/main/scrape.ipynb) Jupyter notebook in this project's repository, which is run as part of [this workflow](https://github.com/palewire/go-big-with-github-actions/blob/main/.github/workflows/second-scraper.yaml#L25-L29).


## Project structure

A typical Framework project looks like this:

```ini
.
├─ src
│  ├─ components
│  │  └─ timeline.js           # an importable module
│  ├─ data
│  │  ├─ launches.csv.js       # a data loader
│  │  └─ events.json           # a static data file
│  ├─ example-dashboard.md     # a page
│  ├─ example-report.md        # another page
│  └─ index.md                 # the home page
├─ .gitignore
├─ observablehq.config.js      # the app config file
├─ package.json
└─ README.md
```

**`src`** - This is the “source root” — where your source files live. Pages go here. Each page is a Markdown file. Observable Framework uses [file-based routing](https://observablehq.com/framework/project-structure#routing), which means that the name of the file controls where the page is served. You can create as many pages as you like. Use folders to organize your pages.

**`src/index.md`** - This is the home page for your app. You can have as many additional pages as you’d like, but you should always have a home page, too.

**`src/data`** - You can put [data loaders](https://observablehq.com/framework/data-loaders) or static data files anywhere in your source root, but we recommend putting them here.

**`src/components`** - You can put shared [JavaScript modules](https://observablehq.com/framework/imports) anywhere in your source root, but we recommend putting them here. This helps you pull code out of Markdown files and into JavaScript modules, making it easier to reuse code across pages, write tests and run linters, and even share code with vanilla web applications.

**`observablehq.config.js`** - This is the [app configuration](https://observablehq.com/framework/config) file, such as the pages and sections in the sidebar navigation, and the app’s title.



## Command reference

| Command           | Description                                              |
| ----------------- | -------------------------------------------------------- |
| `npm install`            | Install or reinstall dependencies                        |
| `npm run dev`        | Start local preview server                               |
| `npm run build`      | Build your static site, generating `./dist`              |
| `npm run deploy`     | Deploy your app to Observable                            |
| `npm run clean`      | Clear the local data loader cache                        |
| `npm run observable` | Run commands like `observable help`                      |


## Installation

Before using this skill, install Playwright and the Chromium browser:

```bash
npm install playwright
npx playwright install chromium
```

This only needs to be done once per environment.



## Authentication

To capture screenshots of authenticated pages (e.g., logged-in GitHub views), you need to save your authentication state first.

### Save Authentication State

Use the `save-auth.cjs` script to log in and save your session:

```bash
node skills/browser-screenshots/scripts/save-auth.cjs \
  --url https://github.com/login \
  --output ~/.playwright/github-auth.json
```

This will:
1. Open a browser window
2. Allow you to log in manually
3. Wait for you to press ENTER in the terminal
4. Save your authentication state (cookies, localStorage, etc.) to the specified file

### Use Saved Authentication

Once saved, use the authentication state with the `--storageState` option:

```bash
node skills/browser-screenshots/scripts/capture.cjs \
  --url https://github.com/new \
  --storageState ~/.playwright/github-auth.json \
  --output docs/_static/github-new-repo.png
```

The authentication state file can be reused for multiple screenshots until your session expires.


## When to Use

Use this skill when the user asks you to:
- Capture a screenshot of a specific URL
- Document a web page or web application state
- Take screenshots of a locally running development server
- Capture a sequence of browser interactions



## How to Capture

Use the Playwright capture script located at `skills/browser-screenshots/scripts/capture.cjs`.

### Basic Screenshot

```bash
node skills/browser-screenshots/scripts/capture.cjs \
  --url https://example.com \
  --output static/screenshots/week-1/example-homepage.png
```

### Common Options

| Option | Description | Default |
|--------|-------------|---------|
| `--url` | URL to capture (required) | - |
| `--output` | Output file path (required) | - |
| `--width` | Viewport width | 1280 |
| `--height` | Viewport height | 800 |
| `--fullpage` | Capture full scrollable page | false |
| `--element` | CSS selector to capture specific element | - |
| `--highlight` | CSS selector to highlight with red border | - |
| `--execute` | JavaScript to run before capture | - |
| `--wait` | Milliseconds to wait before capture | 500 |
| `--dark` | Use dark color scheme | false |

### Examples

**Capture with dark mode:**
```bash
node skills/browser-screenshots/scripts/capture.cjs \
  --url https://code.visualstudio.com \
  --dark \
  --output docs/_static/vscode-homepage.png
```

**Highlight a specific element:**
```bash
node skills/browser-screenshots/scripts/capture.cjs \
  --url https://github.com/new \
  --highlight ".repo-name-input" \
  --output docs/_static/github-repo-name.png
```

**Capture a specific element only:**
```bash
node skills/browser-screenshots/scripts/capture.cjs \
  --url https://example.com \
  --element ".hero-section" \
  --output docs/_static/hero-only.png
```

**Execute JavaScript before capture (e.g., click a button):**
```bash
node skills/browser-screenshots/scripts/capture.cjs \
  --url https://example.com \
  --execute "document.querySelector('button').click()" \
  --wait 1000 \
  --output docs/_static/after-click.png
```

**Full page screenshot:**
```bash
node skills/browser-screenshots/scripts/capture.cjs \
  --url https://example.com \
  --fullpage \
  --output docs/_static/full-page.png
```


## Adding Highlight Boxes

After capturing a screenshot, you can add red highlight boxes to draw attention to specific UI elements using the `add-highlights.cjs` script.

### Finding Coordinates

Use browser developer tools to find element coordinates:
1. Right-click the element and select "Inspect"
2. In the dev tools, hover over the element
3. Note the dimensions shown (e.g., "320 � 48" and position)
4. Calculate: x (left offset), y (top offset), width, height

### Adding Highlights

```bash
node skills/browser-screenshots/scripts/add-highlights.cjs \
  --input docs/_static/screenshot.png \
  --output docs/_static/screenshot-highlighted.png \
  --boxes "295,90,880,90"
```

### Multiple Highlight Boxes

Add multiple `--boxes` parameters to highlight several areas:

```bash
node skills/browser-screenshots/scripts/add-highlights.cjs \
  --input docs/_static/screenshot.png \
  --output docs/_static/screenshot-highlighted.png \
  --boxes "295,90,880,90" \
  --boxes "295,327,880,120"
```

### Custom Styling

```bash
node skills/browser-screenshots/scripts/add-highlights.cjs \
  --input docs/_static/screenshot.png \
  --output docs/_static/screenshot-highlighted.png \
  --boxes "295,90,880,90" \
  --color "#00FF00" \
  --lineWidth 5 \
  --padding 5
```



## Saving Screenshots

Save to `docs/_static/` with descriptive kebab-case filenames.

**Naming convention:** Use kebab-case:
-  `github-new-repo.png`
-  `homepage-hero-section.png`
- L `GitHubNewRepo.png`

**Example structure:**
```
docs/_static/
  github-new-repo.png
  actions-homepage.png
  vscode-settings.png
```


## Embedding in Documentation

When embedding screenshots in the documentation, use standard Markdown image syntax with relative paths:

```markdown
```

For more complex figures with captions, use MyST syntax:

```markdown
```{figure} _static/github-new-repo.png
:alt: GitHub new repository form
:width: 80%

Creating a new repository on GitHub
```
```



## Limitations

- **Cannot capture:** VS Code windows, terminal output, system dialogs (these require manual screenshots)
- **Requires network access:** URLs must be reachable from the machine running the script


## 2025-if-vlookup-google-sheets.md

Using IF and VLOOKUP functions in Google Sheets  
MaryJo Webster  
[maryjo.webster@startribune.com](mailto:maryjo.webster@startribune.com)

Video tutorials are available: [tinyurl.com/mj-data-academy](https://t.co/BtPblHypiG)

Data to go with this class: [tinyurl.com/nicar25-mj-sheets](https://tinyurl.com/nicar25-mj-sheets)



## IF statements

IF() is one of several logical functions in spreadsheet programs. It works the same in Sheets and Microsoft Excel. The basic concept is that you can use it to populate a new column, and have that be different depending on whether it meets the criteria you’ve defined. I find it useful for some basic data cleaning or for categorizing my data.

**Sheet: “BasicIF”**  
This is salary data for the St. Paul Police Department. The city has announced that everyone is going to get a 1% raise, with a minimum of $350. That means that if 1% of a person’s pay is less than $350, they will get the $350. Everyone else will get 1% of their pay. Goal here is to calculate what those raises will be for each person, so we can ultimately add up the dollars. 

Here’s how an IF statement is set up:   
\=IF(logical\_expression, value\_if\_true, value\_if\_false)

The logical\_expression is where you tell it how to figure out which value to ultimately put in the cell. The value\_if\_true is what to put in the new column if the logical\_expression is true and then the value\_if\_false is what to put if it’s false. 

This example is a simple one with only two options. In the next exercise you’ll see that it’s possible to have 3 or more things to evaluate (those are known as nested IF statements)

Here’s the formula we’ll use. The blue part is the logical\_expression, the red is the value if true and the black is value if false.

\=if(F6\*.01\<=350, 350, F6\*.01)

**Sheet: “Nested IF”**

This is data on the results of NFL games from the 2018 season. The data has the scores of each game, but doesn’t have fields identifying which team won the game so we can tally up the totals wins and losses for each team. I also want to add a column that indicates if the home team won or if the visit team won. We also need to deal with tie games because there were several during this season. This is an example of categorizing rows of data – a common thing that is needed for analysis. 

We’ll start by populating the “HomeVisit” column with either “home”, “visit” or “tie” depending on who won the game (or if there’s a tie)

We need to use 2 IF statements. The first one will evaluate whether it was a tie game (we’re doing this first because it’s a simple either/or answer.) The second one determines if the “home” team won or the “visiting” team won.

The blue part is the first IF statement…. Notice there really isn’t a value\_if\_false for that first one. It’s technically the whole second IF statement.

\=if(f2=g2, "tie", if(f2\>g2, "home", "visit"))

A common thing that trips you up with nested IF statements is not getting enough parentheses in there. Always count how many opening ones and make sure you have the same number of closing ones. If you get an error message, first thing to check is number of parentheses and whether they are all in the correct place.

Next, let’s create a column that has the name of the winning team. Notice the names are stored in columns D (home team) and E (visiting team). 

\=if(f2=g2, "tie", if(f2\>g2, d2, e2))

Next, in the column called “Vikings”, let’s just create a “yes” or “no” depending if the row is for the Minnesota Vikings. However we need to use a Nested IF statement because on some rows the Vikings are the home team and others they are the visiting team. So we need to look in both the D column and the E column. 

Notice we start looking in the D column and if it find “Minnesota Vikings”, then it drops a “yes” in the new column. If not, it moves on to the second IF statement and looks in column E.  Note: this relies on the values being consistent and the name of the team appearing exactly like that in both columns. If it’s not consistent, you should either clean it first or there are ways to put a wildcard in this search.

\=if(d2="Minnesota Vikings", "yes", if(e2="Minnesota Vikings", "yes", "no"))


## VLOOKUP 

VLOOKUP is a function that allows you to “join” data from one sheet to another. You can transfer one column of information over to another sheet, matching based on common values. Both sets of data – ideally stored in separate sheets within the same workbook – need to have one column that is the same. 

Sheets: “census\_biz” and “county\_lookup”  
In the “census\_biz” sheet we have partial data from a Census dataset that tallies up the number of workers and businesses in each county, plus total payroll. (this one is kind of old, btw)  Notice that we don’t have the names of the state or the counties. FIPS code 27 is Minnesota, but I don’t know the FIPS codes of the counties (column B). 

In “county\_lookup” we have a code book that translates those county FIPS into names. Our goal is to transfer that name over to the “census\_biz” sheet. 

First, let me explain how VLOOKUP works.   
**\=VLOOKUP(search\_key, range, index, \[is\_sorted\])**

Search\_key is the cell in your data that you want to find a match for. In “census\_biz” that’s going to be B2 – the first value in the county FIPS column. 

Range – this is the range of cells that make up your lookup table. This will be everything from A1:B88 in the “county\_lookup” table. IMPORTANT: the left-most column in this range needs to be the one you are matching/joining on.

Index – this is the number of the column in the “range” that you want to move back to the dataset and drop it in the column where you are typing this formula. Notice I said “number of the column” – I didn’t say the letter. Our range – the data in “county\_lookup”-- consists of 2 columns. So we will tell it we want column 2\. 

\[is\_sorted\] is an optional argument that won’t be needed.

If you Google how to do a VLOOKUP, it won’t include this first step I’m going to show you. But I can guarantee you, my approach saves a lot of headache and simplifies the ultimate formula. 

What we’re going to do is assign a name to the “range.” If we don’t assign a name, we would have to write a complicated jumble to ensure Sheets understands where that A1:B88 is located.   
IMPORTANT: the left-most column of your range needs to be the one you are joining on. Notice that the county FIPS code is the left-most column here. 

Go to the “county\_lookup” sheet and highlight the range of cells we want (everything from A1:B88).  Then right-mouse click and choose “View more cell actions” (all the way at the bottom) and then choose “Define Named Range.” Over on the right it will give you a change to name this area – let’s call it “countynames” .  Click Done. 

Go back to “census\_biz” and in the first blank column, we’ll start building our VLOOKUP.

\=VLOOKUP(B2, countynames, 2\)

Just for giggles, here’s what that formula would have to look like if you DIDN’T use the named range:   
\=vlookup(B2, county\_lookup\!$A$1:$B$88, 2\)

Let’s do another example. This is one I use for some simple data cleanup. 

**Sheets: “death\_data” and “race\_lookup”**

The data in “death\_data” sheet is a cut from Minnesota death certificates of people where opioids were a factor in their deaths. I included just a few of the fields. 

Do a quick pivot table on the “race” column and notice that we’ve got quite a few inconsistencies. When I was prepping this data, I took this column out of the pivot table and pasted it into the sheet that is called “race\_lookup.” Notice that it’s the column called “original.” And then I added a new column where I typed the value I wanted to replace each one with. 

We’ll use a VLOOKUP to match those original values back in the dataset and create a new column where we’ll drop the new values. This is a very easy data cleanup option when you have inconsistencies but it isn’t hundreds of them.

Like we did in the last example, first let’s do the “Define Named Range” step.  Highlight the table in the “race\_lookup’ sheet; right-mouse click, go to More cell actions and then “Define Named Range.”  let’s name this “clean\_race”

Then go back to the “death\_data” worksheet and in the first blank column, let’s drop our VLOOKUP.  
Our matching value is the original race column in H2.   
\=VLOOKUP(h2, clean\_race, 2\)

Optional: You can repeat that last step for the Hispanic ethnicity column. You would do a Pivot Table and copy the column out to a new sheet and make your own lookup table. Then all the other steps would be the same. 

**Sheets: “crime\_data” and “shift\_lookup”**  
This is partial crime incident data in the city of Minneapolis. It has the date and TIME that the call came in, but I want to categorize each row by the shift for the police officers (morning, afternoon or night). This is known as an “inexact” matching situation. The ones we did previously we all exact matches.

Notice the “shift\_lookup” table has the start time of each shift and then a column with the name of the shift that we want to transfer over to the “crime\_data” sheet. 

Setting up a lookup table for an inexact match is a little bit harder than an exact match. Also it has limited applications – mainly dealing with anything numeric: numbers, dates and times. 

When dealing with numbers, the first row of the lookup table needs to have “0” as the first start value. 

In this case, because we’re dealing with time, the first value needs to be midnight. Notice that we have two values for the “night” shift. I’ve purposely made the first value in all capital letters (“NIGHT”) so that you can how the formula is working when it’s applied to the data. 

The first row with “NIGHT” covers midnight to 5:59 a.m.  The second “night” value at the end of the table covers the first half of the night shift from 10 pm to 11:59 p.m. 

First, let’s go to the “shift\_lookup” sheet and define the range. Highlight the little table and right-mouse click to get to “Define Named Range” and let’s call this “shifts”

Next, go back to “crime\_data” and in the first blank column let’s put our VLOOKUP  
\=VLOOKUP(I2, shifts, 2\)

Notice that anything that falls between midnight and 5:59 a.m. has “NIGHT” (in capital letters) and the ones between 10 pm and 11:59 p.m. have “Night” in proper case. If we had created our lookup table starting at 6 am, those midnight to 5:59 records wouldn’t have found a “match” 

If you want your data to be standardized, you can go into the lookup table and change NIGHT to proper case to match the other one and your formula will automatically adjust.



## 2025-news-to-data-journalism.md

New to data journalism? 
Start here
Janelle O’Dea, Illinois Answers Project
Anu Narayanswamy, The Washington Post
Joel Jacobs, ProPublica
MaryJo Webster, Minnesota Star Tribune

Other sessions in the Beginner Track
How to find data (today)
How to request data and documents: FOI (today)
Feed the beast: Integrating data nuggets on deadline (Fri)
Making your data story ironclad (Fri)
Creating meatier stories: Sourcing, documents and other tools to start investigative reporting (Fri)
Tools to save you time (Sat)
Writing with numbers (Sat)
Easy visualizations for your first data stories (Sat)
Taking it all home (Sun)

What is data journalism?

Data journalism doesn’t always involve fancy coding – sometimes it’s a lot of counting 
Series link
Newsletter

Data journalism can be about conveying information in a novel way


Story Link

A data story can be built around a single trend or observation
Story link

Data journalism can be done w/ easier, lighter topics
Gobbled up: Small Missouri turkey farmers see high demand

Christmas trees in St. Louis may be smaller, more costly due to nationwide shortage

And bring clarity, context to serious, recurring issues
‘It wrecked us’: 584 kids killed in St. Louis over 30 years. This grandma knows the cost.

For those living north of Delmar Boulevard, trash complaints addressed at a slower rate

Story link 
It’s great for confirming/quantifying what you’re hearing from human sources

Story link (gift)
Data can help point you in the right direction

What data skills do you need as a beat reporter?

What can you –realistically- learn in your first year?

How do you keep your skills from getting rusty?

How can you add data analysis to your beat reporting?

How do you push yourself beyond wherever your skills are right now?

What are common rookie mistakes?

What do you do if you’re the only person in your newsroom with data skills?

How could I transition from beat reporting to full-time data role?

Q & A
Please go up to the microphone to ask questions

This deck:

Reach out with questions!
MaryJo Webster
Minnesota Star Tribune
maryjo.webster@startribune.com
Anu Narayanswamy
The Washington Post
Joel Jacobs
ProPublica
joel.jacobs@propublica.org
Janelle O’Dea
Illinois Answers


## Useful tools

- [Instaloader](https://instaloader.github.io/), for downloading Instagram posts, comments and profile content.
- [yt-dlp](https://github.com/yt-dlp/yt-dlp), which will download any video from any website ever (mostly)
- [Playwright](https://playwright.dev/), my favorite scraping framework (browser automation!)
- [HAR data extractor](https://jonathansoma.com/har2data/)
- [WARC data extractor](https://jonathansoma.com/warc2data/)



## Tutorials

- [Finding Undocumented APIs](https://inspectelement.org/apis.html)


## Pack-ratting

### HAR files

> This is for Chrome, but is vaguely the same for other browsers. 

Right-click the page and select **Inspect** to open up the developer tools.


Find the Network tab – you might need to resize the window a little bit, or click the >> arrow to find it.


Refresh the page, scroll around, click the download icon.


**You're done!** Now you can head to the [HAR Data Extractor](https://jonathansoma.com/har2data/)

### WACZ files

WACZ/WARC file support is not built into Chrome, so you'll need to download an extension for it. I recommend [Webrecorder ArchiveWeb.page](https://chromewebstore.google.com/detail/webrecorder-archivewebpag/fpeoodllldobpkbkabpblcfaogecpndd?hl=en).

Click the WACZ icon on your menu bar, create a new archiving session under "Save to..." if you feel like it, then click **Start archiving**.


Reload the page to make it start. Scroll around, do whatever. When you're done, click the **Stop archiving** button.

> Supposedly Autopilot will scroll down for you forever, but it doesn't always work.


To download your WACZ file, click **View Archived Pages**, then **Download** on the bottom left. The WACZ file is fine!


**You're done!** Now you can head to the [WARC Data Extractor](https://jonathansoma.com/warc2data/)



## Slides

{{< pdf slides.pdf >}}


## Useful tools 

- [Instaloader](https://instaloader.github.io/), for downloading Instagram posts, comments and profile content.
- [yt-dlp](https://github.com/yt-dlp/yt-dlp), which will download any video from any website ever (mostly)
- [Playwright](https://playwright.dev/), my favorite scraping framework (browser automation!)
- [HAR data extractor](https://jonathansoma.com/har2data/)
- [WARC data extractor](https://jonathansoma.com/warc2data/)



## Tutorials 

- [Finding Undocumented APIs](https://inspectelement.org/apis.html)


## Pack-ratting 

### HAR files 

> This is for Chrome, but is vaguely the same for other browsers.

Right-click the page and select **Inspect** to open up the developer tools.


<p></p>
Right-click, inspect


Find the Network tab -- you might need to resize the window a little bit, or click the \>\> arrow to find it.


<p></p>
Network tab


Refresh the page, scroll around, click the download icon.


<p></p>
Download HAR


**You're done!** Now you can head to the [HAR Data Extractor](https://jonathansoma.com/har2data/)

### WACZ files 

WACZ/WARC file support is not built into Chrome, so you'll need to download an extension for it. I recommend [Webrecorder ArchiveWeb.page](https://chromewebstore.google.com/detail/webrecorder-archivewebpag/fpeoodllldobpkbkabpblcfaogecpndd?hl=en).

Click the WACZ icon on your menu bar, create a new archiving session under "Save to..." if you feel like it, then click **Start archiving**.


<p></p>
Open up WACZ


Reload the page to make it start. Scroll around, do whatever. When you're done, click the **Stop archiving** button.

> Supposedly Autopilot will scroll down for you forever, but it doesn't always work.


<p></p>
Stop archiving with WACZ


To download your WACZ file, click **View Archived Pages**, then **Download** on the bottom left. The WACZ file is fine!


<p></p>
Download your WACZ file


**You're done!** Now you can head to the [WARC Data Extractor](https://jonathansoma.com/warc2data/)



## Slides 

[Download PDF file.](slides.pdf){download=""}


## **`Passive Scraping for`** **`social media`**

(and everything else)

```
onathan Soma
olumbia Journalism School
s4571@columbia.edu
dangerscarf

```

# **`tiers of problem-solving`**


Using a tool

Writing a scraper

Undocumented APIs

Intercepting browser requests

Pack-ratting with HAR and WARC/WACZ files


# **`tiers of problem-solving`**


~~•~~
~~Using a tool~~

~~•~~
Writing a scraper

Undocumented APIs

Intercepting browser requests

Pack-ratting with HAR and WARC/WACZ files


# **`tiers of problem-solving`**


~~•~~
~~Using a tool~~

~~•~~
Writing a scraper

~~•~~
Undocumented APIs

~~•~~
Intercepting browser requests

Pack-ratting with HAR and WARC/WACZ files


# **`the problem`**


Giant files!!!

Chunking!!!

Base64 encoding!!!

Other things I probably don’t even know about yet!!!

(But they do also sometimes work, too, it just depends)




## **`Passive Scraping for`** **`social media`**

(and everything else)

```
onathan Soma
olumbia Journalism School
s4571@columbia.edu
dangerscarf

```


## 2025-quantifying-history.md

Quantifying History
Michael Corey, University of Minnesota
Andrew Ba Tran, Washington Post
Joyce Lee, Washington Post
Alexia Fernández Campbell | Bloomberg Law News
Pratheek Rebala, ProPublica
Jennifer LaFleur, Moderator


Michael Corey, Technical Lead
University of Minnesota Libraries
Thank you very much and for this opportunity to talk about the work of Mapping Prejudice
Mapping Prejudice was founded in 2016 at the University of Minnesota Libraries by a team of historians, librarians, and technologists.
I’ve been with the project for 2 and half years, I was a data journalist for 20 years before that
Data journalists are very used to negotiating for records and turning a pile of record soup into structured data

Warning
Racist and outdated language coming in next slides

Racial covenant
South Minneapolis in 1910
"shall not at any time be conveyed, mortgaged or leased to any person or persons of Chinese, Japanese, Moorish, Turkish, Negro, Mongolian or African blood or decent (sic).”


Benton County
1941, though might be a repeat from earlier
Found by College of St. Benedict professor Brittany Merritt and her students

This one is from Richfield
In 1946 (!) the year after WWII ended


Why should we still care?

Source: Albert Shanker Institute
Albert Shanker Institute
The Albert Shanker Institute is a nonprofit organization established in 1998 to honor the life and legacy of the late president of the American Federation of Teachers.

75%
White families
33%
Black families
Twin Cities metro home ownership
Largest gap in the country
Nationwide: Black home ownership about the same as 1968
And racial covenants are one of the origin points of these disparities and the huge gulf in intergenerational wealth that we are still facing

Covenanted homes:
15% more than non-covenanted
Redlined homes:
25% less than
median value
This is research by Dr. Aradhya Sood and my predecessor Kevin Ehrman-Solberg
In 2019, covenanted houses in Minneapolis were still worth 15% more than non-covenanted houses
White redlined homes worth 25% less than median home value
So this works in both directions – BIPOC people are disadvantaged, but White people gained and continue to enjoy financial advantages
What does that mean? My parents’ house in Wisconsin has a covenant.
So when they sell it someday or if I inherit it someday, and sell it, we will make more money more than 100 years later because of the processes set in motion by this covenants

Mapping Process
Digitized Docs
Digitized Map
Zooniverse
Optical Character Recognition 
Text
So how do we do this?
Digitized images of property records, usually from microfilm
OCR using Amazon Textract
Search for terms associated with racial covenants
Show each “hit” to 5 volunteers on the Zooniverse crowdsourcing platform
They transcribe the text of the covenant, buyer, seller, date, and the property identifying information
Compare each of their responses to determine how confident we are in the answers
Finally we want to put those on a map

Stats to date
~14 million pages processed across 11 counties

60,000+ covenants mapped

11,000 volunteers

52,000 volunteer hours

In conversation with 30+ counties across 10 states + DC

Why crowdsourcing?
It’s more accurate
We don’t have 300 graduate assistants
We do have 11,000+ volunteers
Milwaukee: 200 - 700 transcriptions per day
Peak in 2020: ~2,000 per day
“The 5,000 Fingers of Dr. T.,” 1953
Crowdsourcing is not just faster and more scalable than hiring a couple grad students, it’s also more accurate
But the key thing is you have to be willing to do the community engagement to find crowdsourcing volunteers
But if you build it, and you engage, they will come
Not a muscle that most academics are used to flexing


“The process is the product”
We do our crowdsourcing via weekly Zoom sessions
We train volunteers, explain why this is important
Originally, the idea of the project was to:
A) Get people in front of these primary sources and 
B) Get through all of the data, make the map
At first did these in person, but when the pandemic hit, were forced to try Zoom
Worked much better: fewer technical challenges, more accessible, people can be as visible or low profile as they want to be
We also found that the conversations people were having with each other were really powerful

"This is super tough to read. It makes me emotional. And, it counters that narrative that racism is 'imagined' 
or 'doesn't exist'."

One volunteer stated that it was revelatory, so matter of fact, that it countered the narrative of, "...just pull yourself up 
by your bootstraps."  

"I wasn't surprised that it happened, but to actually see it 
was eye opening"
The process is the product
And this led us to what is now our #1 guiding principle: The Process is the Product
When we started, we assumed that getting to the finished map was the goal.
And we have seen that the map has been transformational in driving very real policy changes.
But our volunteers and other community members have taught us that just mapping covenants is not the real goal.
The real goal and the secret to Mapping Prejudice’s success is the experience of absorbing new information together, talking about that, and that is what opens people to new possibilities for reparative change.
Our volunteers believe strongly – and correctly – that they are owners of this data and this project, and they also show up at meetings and say hey, I learned about this stuff that went down in my neighborhood, and I think it’s time we do things differently and try to fix some of that

How we map matters
How will this map be received? And what does that mean for how we map?
We’re talking about structural racism here
There are so many people who are motivated to not hear this information
So if we color in a lot on this map, we better be sure there was really a covenant there.
Because what happens after we or somebody else makes a map, is that people want to discharge or disavow that covenant on their property
If someone goes through the effort of filing that paperwork, and frankly the emotional processing of this information, and then they find out nope, it was a mistake
It doesn’t take many of those to kill all your goodwill and to allow people to say see, they’re making it up

Covenants per capita in Twin Cities metro
But how are you accounting for history of development?

Property identification is hard (Pls slow your LLM roll)
What is the lot, block, and addition?
Many possible answers
Only one is correct, requires context and additional research
Each individual property really matters
Statistically good is not good enough
Our volunteer crowdsourcing project is really good at this type of problem
We have built-in error checking, and a workflow for manual checks after that
And I would argue that it’s something that an AI-based workflow will really struggle with
There are machine-learning based approaches that can surely get pretty good, statistically, at flagging and even transcribing racial covenants
But statistically good is not good enough

We’re looking for software contractors!
Help us improve “The Deed Machine”
Dev ops: AWS + Terraform
Python/Django
Front-end

corey101@umn.edu,
Or come say hi!

INTRODUCE OURSELVES + ROLES IN STORY 

https://www.washingtonpost.com/video/national/investigations/how-the-post-reported-on-the-smithsonians-brain-collection/2023/08/16/e23a1dd4-393b-44f3-b5d0-f8b22cb95d13_video.html

CLAIRE: how we found the story
NICOLE: how investigative got involved to focus on accountability
ANDREW: how we began gathering records on all human remains to get families and communities in touch with smithsonian

THE COLLECTION
SETS OF HUMAN REMAINS
SMITHSONIAN HUMAN REMAINS
30,700
COUNTRIES
80+
SETS OF HUMAN REMAINS RETURNED
(+2,254 offered for return)
4,068
CLAIRE: information from the smithsonian about how many human remains they have in total, what they’ve repatriated thus far, the majority were taken without consent


THE COLLECTION
MARY SARA
ANDREW: Explain accession card, the work taken to look through all of them and collect them for database, etc 


Pinpoint
Handwriting recognition!

ENTITY EXTRACTION
FOR FREE!
Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents


Google Document AI
Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents


THE COLLECTION
SEARCHABLE DATABASE
Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents

Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents

Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents


BOARDING SCHOOLS
GRAVES FOUND NEAR SCHOOLS
STUDENT DEATHS, BURIAL SITES

SCRAPED MAPS
55,000
FOIA’D RECORDS
20,000
DETAILS SCRAPED FROM FINDAGRAVE
318,00
GOOGLE PINPOINT ACCOUNTS
RECORDS PROCESSED
400,000+
CLAIRE: information from the smithsonian about how many human remains they have in total, what they’ve repatriated thus far, the majority were taken without consent


GENOA INDIAN SCHOOL
Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents

Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents

Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents

EKLUTNA INDUSTRIAL SCHOOL
Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents

SANTEE NORMAL TRAINING SCHOOL
Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents

Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents

Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents

Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents

Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents

Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents

USGS NATIONAL MAP
Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents

Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents


Special Field Order No. 15
The islands from Charleston, south, the abandoned rice fields along the rivers for thirty miles back from the sea, and the country bordering the St. Johns river, Florida, are reserved and set apart for the settlement of the [freedmen] now made free by the acts of war and the proclamation of the President of the United States.


Freedmen’s Bureau
Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents


Freedmen’s Bureau
Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents


Freedmen’s Bureau
Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents


Freedmen’s Bureau
Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents

   Did freedmen get to keep the land they were given? 


Semantic Search 
It is reported that many freedmen refuse to enter into contracts for labor, because they believe that farms will be given them by the U. S. Government. If any do thus believe, they have no reason for their belief. The Government owns no lands in this State. It therefore can give away none. Freedmen can obtain farms with the money which they have earned by their labor. Every one therefore should work diligently, and carefully save his wages, till he may be able to buy land, and possess his own home.


I am beset every day by Freedmen, who are living on this Island, from St. Catherine and other Islands near it in the State of Georgia, wanting to go back to their homes.  These Freed people have been ordered off the Lands on which they have been working and therefore have no where to stay.  I told them than the land in that state might be given to their former owners they say that have rather be there as they have nother here that they can do-can not rent land, they say.  Capt. I think it would be economy for the Bureau to send these people home, or they will have to be taken care of this Spring.


Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents

Describe and Search
“Lists with Names”
Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents

Search by description
“Documents with tables”
Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents


Finding Similar Documents
Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents


Structured prompting
Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents


freedmen.motherjones.com
Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents


Genealogy as Journalism
Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents


Multi Generational Stories
Andrew: Explain what database shows, the decision behind allowing people to search but not presenting all documents


Searching for the 40 Acres


The Landings

Working with public historians & community
TELL US WHEN YOUR STORIES RUN
From a historian’s perspective: You don’t need to prove racism exists
Deep community and historian connections give your work credibility
Your level of trust is likely starting at 0. Journalism’s traditional practices are what got you there.
These should be your collaborators, not your sources
Crediting generously is free
But it’s also time to start paying people
What is in it for your collaborators?
Start by asking what they would like out of this work
Before you have decided what you will do
Community advisory board?
What harmful practices will your org commit to changing?

Thank you!

Presentation at:
bit.ly/NICARHIST25 

Resource list:
z.umn.edu/NICARHIST25tips



## 2025-upping-excel-game.md

# Upping your Excel Game (MaryJo Webster)
_Source: https://sites.google.com/view/mj-basic-data-academy/excel-magic_
_Author: MaryJo Webster (2025 update)_

Intermediate/advanced Excel tutorial and reference guide. Part of MaryJo Webster's Data Journalism Academy.


## Sections
1. Date/time functions
2. String functions
3. Other text functions
4. Logical functions (IF statements)
5. VLOOKUP & XLOOKUP (joining data)
6. Misc: rank(), rounding, percent rank
7. Transpose and using Tableau Reshaper

Practice file: https://www.dropbox.com/scl/fi/aki9p6kif3rxnixm1itcy/ExcelMagic_v2025.xlsx?rlkey=ftotx8few5307ycslsj2m6e6g&st=w86xp1d1&dl=0

Note: Content overlaps with 2020-excel-magic.pdf (same author, updated version).



## Geting Started

### Today's Plan

We'll make a bot that watches for warnings and Slacks them to you.

In the process, you will ...

- Learn about the Weather Service API
- Make your own copy of my code to take home
- Learn about Github Actions
- Learn about Github Codespaces
- Set up Slack to get messages
- Set up Github with the settings you need
- Make it go!

### The slides: A visual guide for where everthing lives

[Slides are here](./slides.pdf).

### The Weather Service API

- Documentation: https://www.weather.gov/documentation/services-web-api
- Click on "Specification"
- Building a URL:
  - Base endpoint: `https://api.weather.gov/alerts/active`
  - We want actual warnings, not tests: `?status=actual`
  - Area: Let's say Minnesota. You can get fancier here, but states are easy: `&area=MN`
  - There's also a "code" option. This is the warning type. Tornado warning, tornado watch, etc. List is [here](https://www.weather.gov/nwr/eventcodes). You could add `&code=TOR` or `@code=TOR,HWW,FFW` for example.
  - Let's leave this tab open

### Make your own copy of my code

In a new browser tab ...

1. Sign into Github (or quickly make an account if you haven't already): [github.com](https://github.com)
1. Return to this page or scroll to the top of this page!
1. Chose the "Fork" button
1. Make sure that the **owner** is now **you**. Click "Create fork"
1. After a minute, you will have a new screen. Note that your name is up at the top! This is your copy. You should use this now. (If you see **jkeefe** instead of your name, you're on the wrong screen. Go find your copy in your github account.)
1. Keep this tab open. We'll call it the **repository tab**.
1. If the `jkeefe` repository is open oinn another tab, close it to avoid confusion.

### Using Codespaces

Normally, when you use Github you _clone_ the code down onto your own computer. Then you type aned code locally. When you're done, you _push_ it back up to Github.

But in this class, we're going to do something different: Code on a computer in the cloud — a computer that's already set up with an environment that works for the code I'm showing you.

This is a temporary, cloud-based computer you use in your browser. You still need to push up your code to the repository save it.

1. Make sure you're on _your_ version of today's repository. You should see your name on at the top of the page (NOT `jkeefe`).
1. Now click the green "<> Code" button and, after you do, the "Codespaces" tab under it.
1. Click "Create Codespace on Main"
1. Wait a minute.
1. We'll be coming back to this tab a lot, and I'll call it the **Codespaces tab**.

### Let's take a look around!

- If you use VS Code, this will look familiar
- Editing happens in the big window
- There's a terminal window at the bottom to run things
- Let's go through the files and folders (skip the Makefile for now)

### Weather Warnings Code

- Look at the Makefile in that folder
- Take a peek at the `SOURCE_URL` at the top
  - If you use this for your work, you'll want to adjust this URL's `area` and `code` values here. See "The Weather Service API" section above.
  - You can also comment out that line, and uncomment line 2 for testing on an old alert I saved
- Open the Terminal, if it's not open already
- Type `make download` ... this downloads everything
- Type `make warnings` ... and see what happens!
- `make clean` clears out what we downloaded so it's fresh
- `make all` does three things: `make clean`, `make download` and `make warnings`

I've already set up Slack to receive my messages. Watch:

- I type `make slack` (this won't work for you ... yet)
- If I do it twice, it won't work. That's good!
- "Seen" warnings are stored in `data/seen.json`

Imagine if we could run this command every few minutes. That'd be pretty useful! :-)


## Making a Warnings Bot

### Understanding the Github Action

Github actions allow you to run your code in the cloud.

_NOTE! This is a **different** computer in the cloud than your Codespace. Technically it's called a "runner" and only exists as long as it takes to run your code._

The driver of any github action is a yaml file in the `.github/workflows` directory of a repository, [like this one](.github/workflows/warnings.yml). Let's take a look.

In your **Codespaces tab**, open the warnings.yml file in the `.github/workflows` directory.

In short, here's what our `warnings` Github Action does:

- It starts running according to a cron statement (here every 10 minutes)
- Spins up a **computer running ubuntu**
- **Checks out** this repository
- **Loads node.js** and installs packages (or it pulls them from a cache if nothing has changed).
- Reads secrets called SLACK_TOKEN and SLACK_CHANNEL ... which we'll set up in a few
- Runs **make all** just like we did in the terminal
- **Commits** the new data and pushes it to the repository (saving our `seen.json` for the next run)

To get this working, you need to do a few key things:

### Change the warnings script we're using

We need to use a slightly more sophisticated warnings script called `warnings-slack.js` instead of `warnings.js`. The new one includes code for sending Slack messages.

We'll adjust our `make all` command to make this change.

- Be sure you're in your **Codespaces tab**.
- On line 4 of your Makefile, where you see `all:`, replace `warnings` with `slack`

It should look like this when you are done:

```
all: clean download slack
```

### Save your work from the Codespace to the repository

In the terminal window (at the bottom of the **Codespaces tab**) ...

- type `git add -A` to add your files to the set you're saving
- type `git commit "set up for slack"` or whatever note makes sense to you for this save
- type `git push origin main` to push up the code, saving it.

### Allow the Action write back to the repository

- Switch to your **repository tab**, the one with `your-name/weather-newsrooms-nicar25` at the top.
- Click through: Settings > Actions > General > Workflow Permissions > Read and write permissions > SAVE
- Don't forget to click "Save!"
  


OK, now we need to set up Slack and get some codes from there.

### Setting up Slack to receive real-time warnings

Slack is a messaging platform used by a lot of newsrooms, and it's surprisingly good at showing messages from robots _and_ is great at managing alerts and messages to your phone, etc.

You'll need to make a Slack _app_ (it's easier than that sounds). And you will need to get a "bot token."

The only catch is that depending on your existing Slack setup, you may need to get an administrator to approve the creation of an app. It _should_ be pretty safe to do: yre only requesting the ability to `chat:write`, which is simply posting into a channel. Many admins are okay with this.

Even if they are not, the good thing is that you this will work in a _free Slack workspace_. So even if you don't have full access to your organization's Slack system, you can do this all on your own if you want. Let's do that for fun:

- Open a new browser tab.
- Go to [slack.com](https://slack.com)
- Chose "Create a new workspace"
- Enter your email
- You'll need to verify your email with a one-time code
- Answer the questions
- Use the "free" option (not "pro")
- Leave this tab open. I'll call this the **Slack workspace tab**.

OK, now we need to make the Slack app. Here's how:

- Open _yet another tab_
- Go to this [Slack app quickstart](https://api.slack.com/start/quickstart) by pasting `https://api.slack.com/start/quickstart` into the new tab
- Do steps 1, 2 and 3
- In step 2, "Requesting Scopes" you just need the `chat:write` scope.
- Note that the bot will only work in channels where the bot is invited (we'll do that in a moment).
- When you are done with all of the steps, the thing you want is the "Bot User OAuth Token" which always starts `oxob-`. That's the token. Copy this into a safe place. If you ever need to get to this token again, go to:
  - Go to https://api.slack.com/apps
  - Sign in if you're not already signed in
  - Click on the app name
  - Click "Install app" on the left side of the screen
  - Copy the "Bot User OAuth Token"
- You can close this tab.

### Make the #alerts channel

Head back to the **Slack workspace tab**.

- In the lefthand column, find and click "Add channels"
- "Create a new channel"
- Call it "#alerts"
- Go to that channel
- Invite the bot to the channel! For example, type: `/invite @warnings_bot` (using whatever you called your bot)
- Next, get the channel ID, which you can find by clicking on the channel name at the very top of the screen.
- The Channel ID is at the very bottom of the pop-up window, and you can click the little copy icon to copy it. Keep it in a safe spot.


### Last steps back at Github

Head back to your Github **repository tab** (not your Codespace)

#### Store your Slack token as a "secret"

We need to let your Github Action know the secret codes to talk to Slack. Github provides a secure vault where you can store these values safely, making them only available to your Actions. Note that for security reasons, you will _not_ be able to see these codes again once you save them here. So be sure they are safely somewhere else. (I keep them in my password manager.)

- Pick: Settings > Secrets and varialbes > Actions > Repository Secrets > New Repository Secret


- Enter `SLACK_TOKEN` in the top box
- Paste your "Bot User OAuth Token" which always starts `oxob-` into the larger box
- Click the "Add Secret" button


#### Store your Slack channel as a "secret"

- Again, you want a New Repository Secret
- This time, enter `SLACK_CHANNEL` in the top box
- Paste your channel ID in the bottom box.

### Run your Action!

Then ... run your action:

- Actions > warnings > Run workflow dropdown > Run workflow button
  
  

- It'll take a few seconds to start.
- Click the "warnings" label next to the yellow dot to watch it work.

You should see something like this appear in the **#alerts** channel in your **Slack workspace tab**:


If you click on the "reply" link, you'll see that the bot has included the details as a thread!


Did the message appear in your Slack workspace? Did the bot throw an error?

If things aren't working, raise your hand. Also you can explore the "Troubleshooting" section below.

Note that if the warning has geodata, you'll get that, too!

### Run the action every 10 minutes

Once it's working, you can make the bot run automatically. Find the `warnings.yml` file in the `.github/workflows` folder.

Then uncomment (so remove the `#` and a single space) from lines 4 and 5. The file should now look exactly like this at the top (the indentations matter and should be exact):

```
name: warnings

on:
  schedule:
    - cron: '*/10 * * * *'   # <-- Set your cron here (UTC). Uses github which can be ~2-10 mins late.
  workflow_dispatch:
```

### Save those changes Codespace to the repository

In the terminal window (at the bottom of the screen) ...

- type `git add -A` to add your files to the set you're saving
- type `git commit "enabled automatic actions"` or whatever note makes sense to you for this save
- type `git push origin main` to push up the code, saving it.

If things are working, you could download the Slack app onto your phone, adjust the notification settings, and you're good to go!



## Troubleshooting

### Try from your Codespace instead of the Action

Go back to your Codespace. You may need to restart it (reload the page and click the restart button).

Your Codespace doesn't know your SLACK_TOKEN and SLACK_CHANNEL secrets, so we need to tell it.

In the terminal window at the bottom, type:

```
export SLACK_TOKEN=[your_token]
```

For example:

```
export SLACK_TOKEN=xoxb-123-456-abc-zyz
```

- In the terminal type:

```
export SLACK_CHANNEL=[channelID] (no spaces)
```

For example:

```
export SLACK_CHANNEL=C123ABC45 (no spaces)
```

- Now type `make all`


## To make the codespace "forget" alerts it's seen

Go into the `data` folder and click on `seen.json`

Replace the contents there with an empty array, which is just a open and closed square bracket, like this:

```
[]
```

Now try `make all` again.



## Saving your work from the Codespace

Your Codespace is an ephemperal computer! It will shut down and then live in your account for a few days. If you don't take any further steps, it will disappear. Which is good!

But to _really_ save your changes, you need to proactively push your code back to your original repository. Here's how:

In the terminal window (at the bottom of the screen) ...

- type `git add -A` to add your files to the set you're saving
- type `git commit "made changes"` or whatever message makes sense to you for this save
- type `git push origin main` to push up the code, saving it.

### Closing up when you're done for the day

Running computers cost money. You get 60 hours free Codespace time every month and 15 gigabytes of storage. The Codespace will shut down after you haven't used it for 30 minutes, but if you'd rather not waste those minutes until it does, you can shut it down like this:

- Go to (github.com/codespaces)[https://github.com/codespaces]
- Pick the three dots next to the Active codespace.
- Chose "Stop codespace"
- Go back to the main tab, and you'll see it's gone
- This is also where you can restart a codespace


## bit.ly/nicar25-weather

### _If you don’t have an Github account, make a free one now at_ _github.com_


bit.ly/nicar25-weather

# **Today’s workshop**


Learn about the Weather Service API
### •
Make your own copy of my code to take home
### •
Learn about Github Actions
### •
Learn about Github Codespaces
### •
Set up Slack to get messages
### •
Set up Github with the settings you need
### •
Make it go
### •


bit.ly/nicar25-weather


# **Notes, links & code**



## bit.ly/nicar25-weather


bit.ly/nicar25-weather

**Github**


**Repository**
jkeefe/weather-newsrooms-nicar25


bit.ly/nicar25-weather

**Github**


**Repository**
jkeefe/weather-newsrooms-nicar25


bit.ly/nicar25-weather

**Github**


**Repository**
jkeefe/weather-newsrooms-nicar25


bit.ly/nicar25-weather

# **Weather Service API**

##### https://www.weather.gov/documentation/services-web-api


bit.ly/nicar25-weather


# **Weather Service API**


bit.ly/nicar25-weather


bit.ly/nicar25-weather


# **Weather Service API**


bit.ly/nicar25-weather

# **Weather Service API**

##### https://api.weather.gov/alerts/active?status=actual&area=MN


bit.ly/nicar25-weather

# **Weather Service API**

##### https://api.weather.gov/alerts/active?status=actual&area=MN


bit.ly/nicar25-weather

# **Weather Service API**

##### https://api.weather.gov/alerts/active?status=actual&area=MN


bit.ly/nicar25-weather

# **Weather Service API**

##### https://api.weather.gov/alerts/active?status=actual&area=MN


bit.ly/nicar25-weather

# **Weather Service API**

##### https://api.weather.gov/alerts/active?status=actual&area=MN


bit.ly/nicar25-weather

# **Weather Service API**

##### https://api.weather.gov/alerts/active?status=actual&area=MN


bit.ly/nicar25-weather


bit.ly/nicar25-weather


**Github**


bit.ly/nicar25-weather

**Github**


bit.ly/nicar25-weather

**Github**


bit.ly/nicar25-weather


bit.ly/nicar25-weather


bit.ly/nicar25-weather

**Github**


bit.ly/nicar25-weather


bit.ly/nicar25-weather

**Github**


**Repository**
your-name/weather-newsrooms-nicar25


bit.ly/nicar25-weather

**Github**


**Repository**
your-name/weather-newsrooms-nicar25


**Locally on Your laptop**


bit.ly/nicar25-weather

**Github**


**Repository**
your-name/weather-newsrooms-nicar25


**Locally on Your laptop**


bit.ly/nicar25-weather

**Github**


**Repository**
your-name/weather-newsrooms-nicar25


**Github Codespaces**


bit.ly/nicar25-weather

**Github**


**Repository**
your-name/weather-newsrooms-nicar25


**Github Codespace**


## 2025-whats-new-llms.md

# What's New in the World of LLMs (NICAR 2025)
_Source: https://simonwillison.net/2025/Mar/8/nicar-llms/_
_Author: Simon Willison_



## Key developments (2022–2025)
- GPT-4 barrier broken by 18 labs in 2024
- Multi-modal capabilities (images, audio, video)
- Pricing collapsed dramatically
- "Inference time compute" / reasoning models (Claude 3.7 Thinking, Gemini 2.0 Thinking)
- Code generation matured: Claude Artifacts, ChatGPT Canvas, "vibe coding"
- Vision LLMs approaching PDF/OCR problem (Gemini, Mistral OCR)
- Local models genuinely useful (Qwen 2.5 Coder, Llama 3.3 70B, Mistral Small 3)


## Takeaways for journalists
1. Develop custom evaluation frameworks
2. Maintain prompt libraries across model versions
3. Leverage vision models for document processing
4. Explore local models for privacy-sensitive work



## (Or, How I Gave Up on OCR Software and Embraced LLMs)
#### Derek Willis, University of Maryland
#### NICAR 25


## https://github.com/dwillis/nicar25-pdfs


## SEND ME BAD PDFS: dwillis@gmail.com


## TL;DR

* Google Gemini Flash 2.0 is now my starting point for extracting text and tables from image PDFs.
* If you want another layer of OCR, AWS Textract is my go-to option
* If you don't want to give your PDFs to Google/Amazon, there are good (but sometimes complex) options!



## The Case for LLMs

Google Gemini has several advantages, but one of them is the absurdly large context window, which means you can upload 100+ page PDFs to it and get to work. It's also pretty cheap and if you want to go the programmatic route, you get 1,500 API calls a day for free. I've been using it for a few months now for PDF parsing and have yet to pay anything.

Other LLMs also do pretty well with image PDFs, and in fact make the case for dumping out the text or performing OCR weaker. They also require us to think about validation strategies.


## Scenario: Electronic PDF, But Multiple Columns

The Maryland Public Secondary School Athletic Association has record books for high school sports in the state. They are electronic PDFs, but they [suck](fall_2023.pdf).


In the past, I would have dumped out the text and then tried to reformat it using pattern matching or a text editor. Now I do this:




## Scenario: Election Results

God Bless Warren County, Pennsylvania, they put individual write-ins in their precinct report, turning it into a 132-page image PDF. I don't want the itemized write-ins, and I want to have some control over the process, so I'll go precinct-by-precinct.

After I establish that Gemini can do the basic stuff (extracting only what I want) right, then I go to formatting it the way I want.


Be deliberate: it's better to ask LLMs to do one thing at a time; in this case, I'm asking for one precinct at a time.

Check out [the result](warren.csv).


## Scenario: News Nerdery Challenge!

Recently, Zack Newman posted this question in the News Nerdery Slack: 


Again, I turned to Gemini, and because the original isn't a classic spreadsheet format, I needed to provide an example of how I wanted the output to look:


Let's check [the results](BlackPop1930.csv).



## Is This Correct?

LLMs are probablistic prediction machines. They get things wrong. How wrong? Yesterday, the French LLM Mistral launched what it called ["the world's best document understanding API"](https://mistral.ai/fr/news/mistral-ocr). I ran the News Nerdery Challenge PDF against it, because that's a tough one. [Here are the results](https://chat.mistral.ai/chat/7b144013-b8c0-4248-a7ce-0635ee822d3e).


The first row looks pretty good - the New York figures are correct except for one percentage - the raw numbers are accurate. Chicago? Only one of the first four numeric columns is correct, and in some cases the differences are large. Oh, look, New York appears again! And Mistral doesn't finish the document.

What you need is a validation plan. Some errors are easy to spot, but what if you have hundreds or thousands of records?

* Random sample spot-checking
* For numeric data, check against aggregate totals
* Repeat the process with the same LLM and compare the two results


## The Lessons

1. Do not speed-run this process. LLMs can quickly produce text, but don't work at that speed; impose a deliberate pace that you control.
2. Be specific in your prompts, and simple beats complex.
3. Your work isn't done when you have results. Have a validation strategy.
4. Consider all of your options; Gemini can be great, but you should try other tools.


