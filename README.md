# piSentinel

Face learning and searching example


### Usage

        Usage::
            python3  piSentinel.py -h shows this help()
            python3  piSentinel.py -t <face_name>  to teach your face to piSentinel
            python3  piSentinel.py -s              to make piSentinel search some known faces
            
        Info:: 
            Press Key 'q' to exit camera frame and save data learning
            
### Dependencies

   python3 [Download](https://www.python.org/downloads/)
   
         virtualenv <env_name>
         source <env_name>/bin/activate
         pip3 install -r requirements.txt
         
### Example

Let´s go to teach pySentinel Hugo´s face:

    python3  piSentinel.py -t Hugo
    
 ![Hugo](c/common/images/icon48.png "Joey Ramone Tablet")
 
 
 When cam start recording and reconice the face pres Q to make piSentinel learnt the face. 
 Learned feaces will be save inside img/ folder. 
 
 Let´s go to search about learnd feace:
 
  ![Ramones](c/common/images/icon48.png "Ramones Tablet")

 





