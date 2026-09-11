"""Generate a local, offline-browsable page of every Higgsfield voice with inline players.

Run:  python build_voice_browser.py
Then open: series/VOICES.html in a browser.

Audio is streamed from Higgsfield's CDN, so this needs an internet connection but no
credits. Published Artifacts cannot play these (the sandbox blocks external media),
which is why this is a plain local file.
"""
import io, os, json

CDN1 = "https://d1xarpci4ikg0w.cloudfront.net"
CDN2 = "https://cdn.higgsfield.ai"

# (name, gender, voice_id, preview_url)
V = [
("Grady","male","e2a2d2e6-9ed2-59cd-82af-feaa27f8a678",CDN1+"/audio_voice/e2a2d2e6-9ed2-59cd-82af-feaa27f8a678/preview-c07e730034d0926d.mp3"),
("Holden","male","3c9d6053-6334-592c-8997-4e325286af3f",CDN1+"/audio_voice/3c9d6053-6334-592c-8997-4e325286af3f/preview-bddba899f043d6a8.mp3"),
("Arthur","male","30fc8796-ceb6-4a66-b3a7-4a145ef7f346",CDN1+"/audio_voice_preset/preview/080fcbab-8be3-4d60-8156-3c3040421e0f.mp3"),
("Archie","male","bd072316-f77c-588b-b6e5-e46b9b03d008",CDN1+"/audio_voice/bd072316-f77c-588b-b6e5-e46b9b03d008/preview-225ae0482643b360.mp3"),
("Fraser","male","6705e465-7b52-5915-a1d8-b1222885e01d",CDN1+"/audio_voice/6705e465-7b52-5915-a1d8-b1222885e01d/preview-b989520a55bc22fd.mp3"),
("Benji","male","e6f9b893-51b1-51d3-afe9-9e0482cb7ac1",CDN1+"/audio_voice/e6f9b893-51b1-51d3-afe9-9e0482cb7ac1/preview-d7f1d3d8ca52125c.mp3"),
("Cillian","male","d8ba9f14-8a24-44db-932b-99e16c45bd32",CDN1+"/audio_voice_preset/preview/0641e334-cdc1-427c-9957-6d0677fb79fd.mp3"),
("Dylan","male","b847bc29-f184-583a-8ad9-d1f1e16d1a60",CDN1+"/audio_voice/b847bc29-f184-583a-8ad9-d1f1e16d1a60/preview-b5fc7cee4a00b4c5.mp3"),
("Reid","male","66469f5a-10db-586a-bab1-72f6ee66ba69",CDN1+"/audio_voice/66469f5a-10db-586a-bab1-72f6ee66ba69/preview-d369773b53804ce8.mp3"),
("Emmett","male","3c7d32be-0182-5c5e-aa6a-663409bfbb26",CDN1+"/audio_voice/3c7d32be-0182-5c5e-aa6a-663409bfbb26/preview-eb4f23d8867ce233.mp3"),
("Desmond","male","563f728c-e249-5a85-97ab-8461e8c09da6",CDN1+"/audio_voice/563f728c-e249-5a85-97ab-8461e8c09da6/preview-df657d3e601522e1.mp3"),
("Cody","male","1ffcdbb3-078b-5491-959d-359e3021e917",CDN1+"/audio_voice/1ffcdbb3-078b-5491-959d-359e3021e917/preview-3907aace99c2401c.mp3"),
("Ian","male","472a562a-4c33-5114-8210-d6ffa1e4e2c5",CDN1+"/audio_voice/472a562a-4c33-5114-8210-d6ffa1e4e2c5/preview-ed06fa132813bf17.mp3"),
("Evan","male","f7a46aa0-183a-5327-b554-e71d8c0071bb",CDN1+"/audio_voice/f7a46aa0-183a-5327-b554-e71d8c0071bb/preview-55ccebc8c46f904a.mp3"),
("Jasper","male","a7b8abe9-47f1-553e-a9df-87945a7e5bc8",CDN1+"/audio_voice/a7b8abe9-47f1-553e-a9df-87945a7e5bc8/preview-1f30d3a4f7854909.mp3"),
("Alden","male","fec5acae-d801-5761-8d2c-4c2c75db3e2a",CDN1+"/audio_voice/fec5acae-d801-5761-8d2c-4c2c75db3e2a/preview-2f4a527ceeb1fc2a.mp3"),
("Knox","male","195e386a-cb61-5c1b-a53b-0e2f0669c408",CDN1+"/audio_voice/195e386a-cb61-5c1b-a53b-0e2f0669c408/preview-cb24afb3a797d372.mp3"),
("Barrett","male","d603a8cd-3fe1-55e0-9245-617a2589131e",CDN1+"/audio_voice/d603a8cd-3fe1-55e0-9245-617a2589131e/preview-00167e6e5fdfbf02.mp3"),
("Landon","male","dc1c0a41-53cd-53af-aec5-ab637840505f",CDN1+"/audio_voice/dc1c0a41-53cd-53af-aec5-ab637840505f/preview-27c57ad4dd45ecde.mp3"),
("Callan","male","d8061b90-ff25-5882-8384-7a6a28806f30",CDN1+"/audio_voice/d8061b90-ff25-5882-8384-7a6a28806f30/preview-fd7abd90cecffdea.mp3"),
("Miles","male","e18664a7-ee4f-5273-acf8-533eb24cd366",CDN1+"/audio_voice/e18664a7-ee4f-5273-acf8-533eb24cd366/preview-0ae20b7a11f4bcc2.mp3"),
("John","male","6b528d43-c056-4a2f-9d82-1591a7ba13b0",CDN2+"/audio_voice/fda261dc-1245-4bba-b47b-4debd425b31a.mp3"),
("Callum","male","858499d9-fef5-40e1-bc29-b4dc661dc283",CDN2+"/audio_voice/40a9b67a-5d11-4f60-91d8-9ae4f3327ff1.wav"),
("Marcus","male","6f98d3dd-324f-4845-8c28-c1d1647a06cd",CDN2+"/audio_voice/cd7a989c-89ba-43c8-bc02-44a8c429825f.wav"),
("Brooks","male","c2acff45-84b2-4974-892d-89fa2d4e5598",CDN1+"/audio_voice_preset/preview/205ba406-f52c-4b61-b3f8-fd04cf683af5.mp3"),
("Gideon","male","1ad38ba4-9cc4-4f2f-9fde-b0fefdf67ae5",CDN1+"/audio_voice_preset/preview/07a76edf-11cb-45dc-b00d-d6deb5fe6901.mp3"),
("Sterling","male","dc382508-c8bd-443c-8cb2-46e57b8d2e6f",CDN1+"/audio_voice_preset/preview/ed37f856-236b-413e-9f4d-9c746648ea72.mp3"),
("Harrison","male","573e5163-59b3-4926-aab1-951ef2985f81",CDN1+"/audio_voice_preset/preview/725aa234-8c64-4a87-8f5e-220aca1375f7.mp3"),
("Alistair","male","d9d5c263-f84e-4752-97b5-3750fcc6fd2f",CDN1+"/audio_voice_preset/preview/1da70cb9-bc0e-4ad4-b812-6e715cb94d6c.mp3"),
("Kevin","male","f1373f24-3b96-433f-9a68-e595810ef608",CDN1+"/audio_voice_preset/preview/f607d671-c0b7-4b2f-96b4-099653af48eb.mp3"),
("Caspian","male","ef70cc83-3015-4bad-9359-0ea968c43ec0",CDN1+"/audio_voice_preset/preview/d7517769-c0f0-4dbf-8faf-07a062ef3526.mp3"),
("Julian","male","95429266-c0ac-4137-a209-63b8812b0f23",CDN1+"/audio_voice_preset/preview/6d53a63c-d1a3-44e2-a6a7-62777b97aa34.mp3"),
("Mark","male","27c04473-84a9-4b60-a41f-c8e8458bd4f1",CDN1+"/audio_voice_preset/preview/808e7f60-bf3b-466e-a81b-f59d54fdac7b.mp3"),
("Orion","male","ed69c516-92d2-4b30-a967-617737a342e5",CDN1+"/audio_voice_preset/preview/4ea32dda-a9b3-4cdc-8021-b827a166ad44.mp3"),
("Andre","male","f1e8226e-2248-4d5f-b43c-0a79e9949dbf",CDN1+"/audio_voice_preset/preview/4fd581a5-5349-447a-842d-1b1ab92bafd9.mp3"),
("Xavier","male","43173c95-3ec8-446a-a162-6504332c578b",CDN1+"/audio_voice_preset/preview/777a5981-c2a6-4b47-aa43-40ab42390f53.mp3"),
("Vlad","male","e5666b9c-99a2-4fac-8b4e-abee078b186d",CDN1+"/audio_voice_preset/preview/55118fe8-5390-4bb2-b0d4-9fef14d91f2b.mp3"),
("Alexey","male","7c2133e5-68ab-511f-9aed-9a67664382b1",CDN2+"/audio_voice_preset/preview/7c2133e5-68ab-511f-9aed-9a67664382b1.mp3"),
("Bob","male","ca12fd00-218c-5198-b10c-7d36e768c12c",CDN2+"/audio_voice_preset/preview/ca12fd00-218c-5198-b10c-7d36e768c12c.mp3"),
("Jake","male","76fe86d8-bf3a-5ed8-ba52-f793b29cf71f",CDN2+"/audio_voice_preset/preview/76fe86d8-bf3a-5ed8-ba52-f793b29cf71f.mp3"),
("Ken","male","ceee41dc-0ee8-59a7-b3e8-2744116fcb5e",CDN2+"/audio_voice_preset/preview/ceee41dc-0ee8-59a7-b3e8-2744116fcb5e.mp3"),
("Luc","male","04e867c7-9e41-5cff-80d3-5284e74d7bd1",CDN2+"/audio_voice_preset/preview/04e867c7-9e41-5cff-80d3-5284e74d7bd1.mp3"),
("Ainsley","female","731b4ffe-e95e-59f4-8c00-81608936091f",CDN1+"/audio_voice/731b4ffe-e95e-59f4-8c00-81608936091f/preview-37d345ad8f2edf91.mp3"),
("Brielle","female","a00bc7f3-0236-5e76-ac65-90137ce0f5a4",CDN1+"/audio_voice/a00bc7f3-0236-5e76-ac65-90137ce0f5a4/preview-b3150d3b115505cd.mp3"),
("Faye","female","d198dc0b-c4e5-5198-aa1d-ecf5ca0927c4",CDN1+"/audio_voice/d198dc0b-c4e5-5198-aa1d-ecf5ca0927c4/preview-2c0cfabdc015c510.mp3"),
("Delia","female","1550321e-7f5b-526e-b001-02328b03e9bc",CDN1+"/audio_voice/1550321e-7f5b-526e-b001-02328b03e9bc/preview-b15652c223395257.mp3"),
("Celine","female","57ccb351-84d7-54ba-afd4-26b566ca6023",CDN1+"/audio_voice/57ccb351-84d7-54ba-afd4-26b566ca6023/preview-b8a818f93ce2e187.mp3"),
("Elodie","female","8b95a259-62fd-545d-b0f0-7b521a972b6b",CDN1+"/audio_voice/8b95a259-62fd-545d-b0f0-7b521a972b6b/preview-e89a9628612d9022.mp3"),
("Ginger","female","8d261e04-3a3a-5853-96fc-0d89cca28bb4",CDN2+"/audio_voice_preset/preview/8d261e04-3a3a-5853-96fc-0d89cca28bb4.mp3"),
("Giselle","female","9d3128b8-dd25-5158-9bdb-2e69ac8998b9",CDN1+"/audio_voice/9d3128b8-dd25-5158-9bdb-2e69ac8998b9/preview-4b6e10df2694cd55.mp3"),
("Helena","female","3c2b83c0-2e0a-5ae8-998a-a5fe71b7eccd",CDN1+"/audio_voice/3c2b83c0-2e0a-5ae8-998a-a5fe71b7eccd/preview-23723fb8dfc918c6.mp3"),
("Isla","female","7367e919-3069-5a0b-939e-dfb1c0fd91b4",CDN1+"/audio_voice/7367e919-3069-5a0b-939e-dfb1c0fd91b4/preview-48b702b4d554cd90.mp3"),
("Juno","female","a3ce02fe-4d3e-55bc-b4d4-a4801b9acdb4",CDN1+"/audio_voice/a3ce02fe-4d3e-55bc-b4d4-a4801b9acdb4/preview-973131fd185713d9.mp3"),
("Maeve","female","64cf4f1a-61c8-5938-9aea-83d12b2e1d13",CDN1+"/audio_voice/64cf4f1a-61c8-5938-9aea-83d12b2e1d13/preview-beb7ec12bc6be2ca.mp3"),
("Nadine","female","165d9309-bb17-56ff-964a-5d6a38dab92f",CDN1+"/audio_voice/165d9309-bb17-56ff-964a-5d6a38dab92f/preview-964c0d3a724d5c0f.mp3"),
("Opal","female","66f35c82-2088-55eb-a0aa-7bf715dc03b7",CDN1+"/audio_voice/66f35c82-2088-55eb-a0aa-7bf715dc03b7/preview-bc614761886f9553.mp3"),
("Petra","female","0c63637d-2ecb-5bda-9bbe-38894aa9a876",CDN1+"/audio_voice/0c63637d-2ecb-5bda-9bbe-38894aa9a876/preview-491aff05b209df72.mp3"),
("Raina","female","1c3a4775-9afb-52c1-a2bf-b6543231a9a1",CDN1+"/audio_voice/1c3a4775-9afb-52c1-a2bf-b6543231a9a1/preview-dddcd66df049ecdd.mp3"),
("Romy","female","2e5f5f01-6d50-5335-a9ae-e8f81cd42342",CDN1+"/audio_voice/2e5f5f01-6d50-5335-a9ae-e8f81cd42342/preview-8fa4cea7f0b36f7e.mp3"),
("Soraya","female","5c1d2f7f-cdb4-5b1d-bca9-156439e3275e",CDN1+"/audio_voice/5c1d2f7f-cdb4-5b1d-bca9-156439e3275e/preview-bea68c38c833903b.mp3"),
("Talia","female","05bd642c-3e9d-55a1-aa26-43fea30a3e94",CDN1+"/audio_voice/05bd642c-3e9d-55a1-aa26-43fea30a3e94/preview-7f7cc1ce645c15fe.mp3"),
("Livia","female","984ddbed-83d3-5388-84ce-02fe6c24befa",CDN1+"/audio_voice/984ddbed-83d3-5388-84ce-02fe6c24befa/preview-33230197ddec20fe.mp3"),
("Daisy","female","032386ec-491b-5bdc-81ac-49e9a6a2c89d",CDN1+"/audio_voice/032386ec-491b-5bdc-81ac-49e9a6a2c89d/preview-349c8b03d258a143.mp3"),
("Una","female","e91c5696-3d9f-5ae6-9c68-8389d2d0d294",CDN1+"/audio_voice/e91c5696-3d9f-5ae6-9c68-8389d2d0d294/preview-cd9c4a84ed2b1aba.mp3"),
("Evie","female","7a6845a2-5865-5669-a0ca-8fc8d8e96528",CDN1+"/audio_voice/7a6845a2-5865-5669-a0ca-8fc8d8e96528/preview-fd9231b9595685cd.mp3"),
("Kaia","female","bb9db352-f345-59f3-90b3-fa9432bcff91",CDN1+"/audio_voice/bb9db352-f345-59f3-90b3-fa9432bcff91/preview-736bb7b23c693fc2.mp3"),
("Vera","female","0c51919f-0756-5f8d-8169-026a339d8fd7",CDN1+"/audio_voice/0c51919f-0756-5f8d-8169-026a339d8fd7/preview-b33f1e08e41153ee.mp3"),
("Gracie","female","09878754-f20b-5330-9790-58a8027ab5b2",CDN1+"/audio_voice/09878754-f20b-5330-9790-58a8027ab5b2/preview-b3f85cf93cb99d3a.mp3"),
("Hallie","female","10274bf1-fb93-554f-b59f-d620a920fd36",CDN1+"/audio_voice/10274bf1-fb93-554f-b59f-d620a920fd36/preview-cab7f724896d7e00.mp3"),
("Willow","female","f878bf3f-115b-5842-8934-c789c7947733",CDN1+"/audio_voice/f878bf3f-115b-5842-8934-c789c7947733/preview-044549d8844d0c6f.mp3"),
("Xenia","female","fccb005b-c9f2-5b0e-b6cb-3e64edcbbf78",CDN1+"/audio_voice/fccb005b-c9f2-5b0e-b6cb-3e64edcbbf78/preview-c7a5b65cbbda79a9.mp3"),
("Yara","female","fd25dc29-6495-5df3-9332-26bb58fdd575",CDN1+"/audio_voice/fd25dc29-6495-5df3-9332-26bb58fdd575/preview-ebb4231829b553cb.mp3"),
("Annie","female","f2801b0f-e345-598e-86f5-8364d886d96b",CDN1+"/audio_voice/f2801b0f-e345-598e-86f5-8364d886d96b/preview-9e016517ced87238.mp3"),
("Zelda","female","b7aaea29-0c88-5925-90c0-8f66754cda53",CDN1+"/audio_voice/b7aaea29-0c88-5925-90c0-8f66754cda53/preview-ba49e555851471ec.mp3"),
("Bella","female","eba85120-4ed5-5202-a6f6-696e2c6fe2b6",CDN1+"/audio_voice/eba85120-4ed5-5202-a6f6-696e2c6fe2b6/preview-9973ca34ac673969.mp3"),
("Cora","female","8c4760aa-b4d2-5313-90a9-01f2d3eecd20",CDN1+"/audio_voice/8c4760aa-b4d2-5313-90a9-01f2d3eecd20/preview-38900ed6b3b4d2bf.mp3"),
("Emily","female","6b3e3642-f7b7-4cb8-9688-51e233c4b92f",CDN2+"/audio_voice/6cf1cf4b-8fd5-4ef2-abb7-10e43b2aa9be.mp3"),
("Naomi","female","caeba733-3c17-43db-863e-69c7025512cd",CDN2+"/audio_voice/bfe496ad-1296-441e-9ba6-02cfe4761eb3.wav"),
("Onyx","female","8911390e-4b59-459b-ba84-19010917e1df",CDN2+"/audio_voice/047111ca-5440-4693-b6b0-e4eac6ecb61b.wav"),
("Pixie","female","0178ef57-ada4-43d9-992b-8d9221045bb4",CDN2+"/audio_voice/bbc48402-e8e3-4639-9aae-949020a792a5.mp3"),
("Remy","female","b9c5c5db-4eb7-468a-a0b7-d06423af0335",CDN2+"/audio_voice/a6457f72-a05b-421c-8487-7f38cd532dfb.wav"),
("Tamsin","female","9eb5a147-c322-4f8a-8bc5-a30679dfaf5c",CDN2+"/audio_voice/a356efae-457f-4425-bd57-0b6db18e5aee.wav"),
("Kayla","female","5c615d8a-5135-539d-8ab0-497b7ceabbae",CDN2+"/audio_voice_preset/preview/5c615d8a-5135-539d-8ab0-497b7ceabbae.mp3"),
("Ines","female","023ebf5e-1970-40d8-825c-a5ef6a1dd4ff",CDN2+"/audio_voice/a35522bb-1734-4a80-8e5f-64c05f1148a8.wav"),
("Marisol","female","75e72cd5-011b-4130-a474-e8b1ab341f04",CDN2+"/audio_voice/e64e0720-9d99-4873-aae5-7d86a803246c.wav"),
("Roxie","female","f6448975-768e-4327-b932-1b7c973d58e9",CDN1+"/audio_voice_preset/preview/13633b42-3603-4422-b64d-e56ef39104b9.mp3"),
("Tallulah","female","f32c8f51-449e-4ddf-bdf7-1527e11df917",CDN1+"/audio_voice_preset/preview/6d9fab46-e2ce-481e-8433-9bfdac49dca0.mp3"),
("Hana","female","c25f78a0-714e-42af-8da3-a399cef94968",CDN1+"/audio_voice_preset/preview/3a978518-1fae-451e-bc30-08cb35b0d79f.mp3"),
("Skye","female","1fb253b8-928b-4d29-a349-f242a71eaddf",CDN1+"/audio_voice_preset/preview/86e9dea6-6196-41a2-8856-e7c21df4e8cd.mp3"),
("Mabel","female","fa64fba4-ad02-405e-99d0-1f085d87c706",CDN1+"/audio_voice_preset/preview/3fa43fdc-2284-42db-a25b-c24a7263a213.mp3"),
("Maya","female","b0f766b7-8703-4bd1-b973-f857c36837b6",CDN1+"/audio_voice_preset/preview/dc8d2759-bb32-4b0e-904d-b8873efc958e.mp3"),
("Quinn","female","80914268-dfae-4f76-8306-36f2d55f58f8",CDN1+"/audio_voice_preset/preview/9b7f84c7-8b42-4a32-a0f1-ba223bfd5fae.mp3"),
("Imogen","female","3811e986-0891-47cf-a1f5-78a1d62a547a",CDN1+"/audio_voice_preset/preview/0112058f-8bd6-423a-aa69-28112d237ac1.mp3"),
("Zoe","female","d0374db1-44b9-4f05-939e-0a9ae9dbbe6a",CDN1+"/audio_voice_preset/preview/49455cd5-64e8-4578-8531-f1262f8b338b.mp3"),
("Gia","female","530df032-c311-483b-a750-cb3c9e1bcdfd",CDN1+"/audio_voice_preset/preview/19581df2-5796-49ed-9cdd-b7ef5afe5626.mp3"),
("Sloane","female","b57b22a0-f287-405b-bc82-6f08f5e6bb1f",CDN1+"/audio_voice_preset/preview/b504d232-3e67-489d-9b22-0b927caa5926.mp3"),
("Luna","female","375a3398-e3b4-4f91-845d-42181e352899",CDN1+"/audio_voice_preset/preview/b3b5b2a1-7606-4e40-ac69-bf0ba43d3840.mp3"),
("Vesper","female","c3204739-4084-41a3-9dc5-c805b307ec18",CDN1+"/audio_voice_preset/preview/1f362462-0a34-41c6-ad26-27525eb5a3cd.mp3"),
("Chloe","female","e9cfbbf0-4476-46be-b396-596eb774b165",CDN1+"/audio_voice_preset/preview/6851db6f-4e33-422a-a5c9-68e1e01cc83a.mp3"),
("Elena","female","ca83ca7f-c186-493d-bd69-0d765fa861b2",CDN1+"/audio_voice_preset/preview/1f743d5b-f5f5-4add-a124-1de7c176a531.mp3"),
("Nora","female","d081b915-6623-4a44-bacf-80d0f1c90a03",CDN1+"/audio_voice_preset/preview/7d7c4a2e-0e79-4eb2-b695-e1de5831f27e.mp3"),
("Sienna","female","41023a48-71ab-478a-bea7-c7b5a78f6b36",CDN1+"/audio_voice_preset/preview/5c1ab4a7-405e-4237-a126-3b94d8ba7d8c.mp3"),
("Amanda","female","22aeaea5-3677-5fd7-b932-34f362087a9b",CDN2+"/audio_voice_preset/preview/22aeaea5-3677-5fd7-b932-34f362087a9b.mp3"),
("Anika","female","4b2dc8f3-5e8b-59a9-9a5c-85620e44c033",CDN2+"/audio_voice_preset/preview/4b2dc8f3-5e8b-59a9-9a5c-85620e44c033.mp3"),
("Anush","female","cee3e562-e2ec-59cc-bf78-023930560e51",CDN2+"/audio_voice_preset/preview/cee3e562-e2ec-59cc-bf78-023930560e51.mp3"),
("Judy","female","3375c7b3-8e04-5d44-9e09-33532864477d",CDN2+"/audio_voice_preset/preview/3375c7b3-8e04-5d44-9e09-33532864477d.mp3"),
("Karen","female","b483a172-2776-559b-b138-8853559b20ee",CDN2+"/audio_voice_preset/preview/b483a172-2776-559b-b138-8853559b20ee.mp3"),
("Kiki","female","2d51d9d0-b2a4-5e8b-9c63-f310adafd5f7",CDN2+"/audio_voice_preset/preview/2d51d9d0-b2a4-5e8b-9c63-f310adafd5f7.mp3"),
("Olena","female","3d1cdbad-25ef-5a04-93d9-b29be1b91299",CDN2+"/audio_voice_preset/preview/3d1cdbad-25ef-5a04-93d9-b29be1b91299.mp3"),
("Liza","female","1e7feef5-2436-55bd-8778-cb075ecd081e",CDN2+"/audio_voice_preset/preview/1e7feef5-2436-55bd-8778-cb075ecd081e.mp3"),
("Lucy","female","6acca956-f45a-55cb-8a6e-e34fa85a03b0",CDN2+"/audio_voice_preset/preview/6acca956-f45a-55cb-8a6e-e34fa85a03b0.mp3"),
("Linda","female","f82790fd-8283-5187-9e3f-cc8e99bc5b17",CDN2+"/audio_voice_preset/preview/f82790fd-8283-5187-9e3f-cc8e99bc5b17.mp3"),
("Isabella","female","80924413-1ea8-4e64-9719-e00b86796f05",CDN1+"/audio_voice_preset/preview/120c0cd2-250c-40c8-937e-f31bfe87150d.mp3"),
]

# what we actually know, rather than guesses
NOTES = {
 "Cillian": ("locked", "MOONEY's voice - already applied to 17 shots"),
 "Chloe":   ("was",    "Raichu's original voice in Fowl Play (young female)"),
 "Benji":   ("young",  "tagged YOUNG male in Higgsfield metadata"),
 "Miles":   ("mid",    "tagged middle-aged - Mooney's first voice, too deep"),
 "Holden":  ("mid",    "tagged middle-aged - used on Lucky Lots"),
 "Grady":   ("mid",    "tagged middle-aged - used on Lucky Lots"),
 "Brooks":  ("mid",    "tagged middle-aged"),
 "Nora":    ("was",    "the neighbour's voice in Fowl Play"),
 "Pixie":   ("young",  "tagged young female"),
 "Vesper":  ("mid",    "tagged middle-aged female"),
 "Luna":    ("young",  "tagged young female"),
}

CARD = """<div class="v" data-n="{n}" data-g="{g}">
  <div class="hd"><span class="nm">{n}</span><span class="g {g}">{g}</span>{badge}</div>
  <audio preload="none" controls src="{u}"></audio>
  <button class="id" data-id="{i}" title="click to copy">{i}</button>
  {note}
</div>"""

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    cards = []
    for n, g, i, u in V:
        kind, txt = NOTES.get(n, ("", ""))
        badge = '<span class="b %s">%s</span>' % (kind, kind) if kind else ""
        note = '<p class="note">%s</p>' % txt if txt else ""
        cards.append(CARD.format(n=n, g=g, i=i, u=u, badge=badge, note=note))
    html = TEMPLATE.replace("__CARDS__", "\n".join(cards))\
                   .replace("__COUNT__", str(len(V)))\
                   .replace("__M__", str(sum(1 for v in V if v[1] == "male")))\
                   .replace("__F__", str(sum(1 for v in V if v[1] == "female")))
    out = os.path.join(here, "VOICES.html")
    io.open(out, "w", encoding="utf-8").write(html)
    print("wrote %s  (%d voices)" % (out, len(V)))

TEMPLATE = """<!doctype html><html><head><meta charset="utf-8">
<title>Higgsfield Voices</title>
<style>
:root{--bg:#EDF0F3;--card:#fff;--ink:#16202B;--mute:#6F7C88;--rule:#CBD4DB;--acc:#4F63B8;--f:#B14E33}
@media(prefers-color-scheme:dark){:root{--bg:#121A22;--card:#1E2A35;--ink:#E6EDF2;--mute:#8797A4;--rule:#2E3D4A;--acc:#93A4EA;--f:#E08D6E}}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font:15px/1.5 system-ui,-apple-system,Segoe UI,sans-serif;margin:0;padding:24px}
h1{font-size:26px;margin:0 0 4px}
.sub{color:var(--mute);margin:0 0 20px}
.bar{position:sticky;top:0;background:var(--bg);padding:12px 0;border-bottom:1px solid var(--rule);margin-bottom:20px;z-index:5;display:flex;gap:10px;flex-wrap:wrap;align-items:center}
button.f{background:var(--card);border:1px solid var(--rule);color:var(--ink);padding:7px 15px;border-radius:20px;cursor:pointer;font-size:14px}
button.f.on{background:var(--acc);color:#fff;border-color:var(--acc)}
#q{flex:1;min-width:180px;padding:8px 12px;border:1px solid var(--rule);border-radius:20px;background:var(--card);color:var(--ink);font-size:14px}
#count{color:var(--mute);font-size:13px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:14px}
.v{background:var(--card);border:1px solid var(--rule);border-radius:10px;padding:13px}
.v.hide{display:none}
.hd{display:flex;align-items:center;gap:8px;margin-bottom:9px;flex-wrap:wrap}
.nm{font-weight:600;font-size:17px}
.g{font-size:10px;text-transform:uppercase;letter-spacing:.08em;padding:2px 7px;border-radius:3px}
.g.male{background:rgba(79,99,184,.16);color:var(--acc)}
.g.female{background:rgba(177,78,51,.16);color:var(--f)}
.b{font-size:10px;text-transform:uppercase;letter-spacing:.08em;padding:2px 7px;border-radius:3px;background:rgba(55,121,107,.18);color:#37796B}
@media(prefers-color-scheme:dark){.b{color:#6FB6A4}}
.b.locked{background:rgba(177,78,51,.2);color:var(--f)}
audio{width:100%;height:34px;margin-bottom:8px}
button.id{width:100%;font:11px ui-monospace,Menlo,monospace;background:transparent;border:1px dashed var(--rule);color:var(--mute);padding:5px;border-radius:5px;cursor:pointer;text-align:left;overflow:hidden;text-overflow:ellipsis}
button.id:hover{border-color:var(--acc);color:var(--acc)}
button.id.copied{border-style:solid;border-color:#37796B;color:#37796B}
.note{margin:7px 0 0;font-size:12.5px;color:var(--mute)}
</style></head><body>
<h1>Higgsfield voices</h1>
<p class="sub">__COUNT__ presets — __M__ male, __F__ female. Click a voice ID to copy it. Only one clip plays at a time.</p>
<div class="bar">
  <button class="f on" data-f="all">All</button>
  <button class="f" data-f="male">Male</button>
  <button class="f" data-f="female">Female</button>
  <input id="q" placeholder="search by name…">
  <span id="count"></span>
</div>
<div class="grid">
__CARDS__
</div>
<script>
var cards=[].slice.call(document.querySelectorAll('.v')),filt='all',q='';
function apply(){var n=0;cards.forEach(function(c){
  var okG=filt==='all'||c.dataset.g===filt,
      okQ=!q||c.dataset.n.toLowerCase().indexOf(q)>-1;
  var show=okG&&okQ; c.classList.toggle('hide',!show); if(show)n++;});
  document.getElementById('count').textContent=n+' shown';}
document.querySelectorAll('button.f').forEach(function(b){b.onclick=function(){
  document.querySelectorAll('button.f').forEach(function(x){x.classList.remove('on')});
  b.classList.add('on'); filt=b.dataset.f; apply();};});
document.getElementById('q').oninput=function(e){q=e.target.value.toLowerCase().trim();apply();};
document.addEventListener('play',function(e){
  document.querySelectorAll('audio').forEach(function(a){if(a!==e.target)a.pause();});},true);
document.querySelectorAll('button.id').forEach(function(b){b.onclick=function(){
  navigator.clipboard.writeText(b.dataset.id).then(function(){
    var t=b.textContent; b.textContent='copied'; b.classList.add('copied');
    setTimeout(function(){b.textContent=t;b.classList.remove('copied');},900);});};});
apply();
</script></body></html>"""

if __name__ == "__main__":
    main()
