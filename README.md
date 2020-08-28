# i-am-sleepy-af



This is a readme for a CNN pokemon identifier. And the title justifies the situation i am currently in, extremely sleepy. Faiza used to hate pokemons so i designed this. Notes :
* cv2 has problems in reading some images which is why the preprocessing filters out the error causing images.
* The accuracy is very low just because i am training the model with one sample each.
* Me being a rookie, couldn't figure out why there was a matrix mismatch at the output layer. The resultant vector had to be 1 into 1 matrix but my dumb ass had set       the thing to output a 1 into 720 matrix.
* Do tell me how the model works if someone tries it on more than one samples.
