# Rock-Paper-Scissor-Game
Engineered this simple yet fun game using OpenCV and Hand Landmarks Detection Model

This project has been built using MediaPipe and OpenCV. The MediaPipe framework is mainly used for rapid prototyping of perception pipelines with AI models for inferencing and other reusable components. It also facilitates the deployment of computer vision applications.

**MediaPipe** offers two models for detection. The **Palm Detection model** locates hands within the input image, and the **Hand Landmarks Detection model** identifies specific hand landmarks on the cropped hand image defined by the Palm Detection model.

**Understanding the Hand Landmark Detection Model**
It allows you to detect the landmarks of the hands in an image. You can use this task to locate key points of hands and render visual effects on them. This task operates on image data with a machine learning (ML) model as static data or a continuous stream and outputs hand landmarks in image coordinates, hand landmarks in world coordinates, and the handedness of multiple detected hands.

### Parameters it primarily works on

- **static_image_mode**: If set to false, the solution treats the input image as a video stream.
- **max_num_hands**: The maximum number of hands that can be detected by the model; the default value is 2.
- **model_complexity**: Landmark accuracy depends on this parameter, which ranges between 0 and 1. The default value is 1.
- **min_detection_confidence**: The minimum value for which the detection should be considered successful, ranging from 0 to 1. The default value is 0.5.
- **min_tracking_confidence**: The minimum value for tracking confidence, ranging from 0 to 1. The default value is 0.5.

Overview of the Game:
 This is the classic rock paper scissor game, where the user can use their web cam to show the gesture (rock,paper or scissor) and compete with the computer. To start a new round, the user need to press the 'q' key which resets the timer to 0. After 3 seconds, the user's hand gesture and the machine's random choice is displayed and scores are updated.

The screenshots attached below show a clear demonstration of this game.

![Screenshot (445)](https://github.com/user-attachments/assets/300f517d-04d6-43d8-8835-482f564f08a1)

![Screenshot (446)](https://github.com/user-attachments/assets/c78d63fe-d303-4bb8-ab51-0ee808ad6504)

![Screenshot (447)](https://github.com/user-attachments/assets/b790d9a7-4257-4dd3-8faa-2d9e8f672803)

![Screenshot (440)](https://github.com/user-attachments/assets/0f0e03ed-0ef8-498e-8e17-e4ee7e21807a)


