# i-am-sleepy-af

Sorry for not mentioning the dataset i used. I don't have the energy to actually search it right now. Will sure tomorrow morning.

(I don't have a powerful machine which forces me to reduce the image sizes to 70 into 70 pixels at max. This might be affecting accuracy of the model. Edit the resize sizes according to your machine.)

This is a readme for a CNN pokemon identifier. And the title justifies the situation i am currently in, extremely sleepy. Faiza used to hate pokemons so i designed this. Notes :
* cv2 has problems in reading some images which is why the preprocessing filters out the error causing images.
* The accuracy is very low just because i am training the model with one sample each.
* Me being a rookie, couldn't figure out why there was a matrix mismatch at the output layer. The resultant vector had to be 1 into 1 matrix but my dumb ass had set       the thing to output a 1 into 720 matrix.
* Do tell me how the model works if someone tries it on more than one samples.
