# ChatBot
chat bot using deep learning techniques

Reffered this:- https://github.com/Conchylicultor/DeepQA


# Chatbot

To train the model, simply run main.py. Once trained, you can test the results with main.py --test (results generated in 'save/model/samples_predictions.txt') or main.py --test interactive (more fun).

Here are some flags which could be useful. For more help and options, use python main.py -h:

    --modelTag <name>: allow to give a name to the current model to differentiate between them when testing/training.
    --keepAll: use this flag when training if when testing, you want to see the predictions at different steps (it can be interesting to see the program changes its name and age as the training progress). Warning: It can quickly take a lot of storage space if you don't increase the --saveEvery option.
    --filterVocab 20 or --vocabularySize 30000: Limit the vocabulary size to and optimize the performances and memory usage. Replace the words used less than 20 times by the <unknown> token and set a maximum vocabulary size.
    --verbose: when testing, will print the sentences as they are computed.
    --playDataset: show some dialogue samples from the dataset (can be use conjointly with --createDataset if this is the only action you want to perform).

To visualize the computational graph and the cost with TensorBoard, just run tensorboard --logdir save/.

By default, the network architecture is a standard encoder/decoder with two LSTM layers (hidden size of 256) and an embedding size for the vocabulary of 32. The network is trained using ADAM. The maximum sentence length is set to 10 words, but can be increased.

# Web interface
 Once trained, it's possible to chat with it using a more user friendly interface. The server will look at the model copied to save/model-server/model.ckpt. The first time you want to use it, you'll need to configure it with:

export CHATBOT_SECRET_KEY="my-secret-key"
cd chatbot_website/
python manage.py makemigrations
python manage.py migrate

Then, to launch the server locally, use the following commands:

cd chatbot_website/
redis-server &  # Launch Redis in background
python manage.py runserver

After launch, the interface should be available on http://localhost:8000/. If you want to deploy the program on a server, use python manage.py runserver 0.0.0.0

# Link to the pre-trained weights- https://drive.google.com/file/d/0Bw-phsNSkq23OXRFTkNqN0JGUU0/view?usp=sharing



