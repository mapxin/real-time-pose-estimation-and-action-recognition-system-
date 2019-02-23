# coding=utf8


def joint_completion(joint):
    if 0 not in joint:
        joint[0] = (0, 0)
    
    if 1 not in joint:
        joint[1] = (0, 0)
    
    if 2 in joint and 5 not in joint:
        joint[5] = joint[2]
    elif 2 not in joint and 5 in joint:
        joint[2] = joint[5]
    elif 2 not in joint and 5 not in joint:
        joint[2] = joint[5] = (0, 0)
        
    if 3 in joint and 6 not in joint:
        joint[6] = joint[3]
    elif 3 not in joint and 6 in joint:
        joint[3] = joint[6]
    elif 3 not in joint and 6 not in joint:
        joint[3] = joint[6] = (0, 0)
        
    if 4 in joint and 7 not in joint:
        joint[7] = joint[4]
    elif 4 not in joint and 7 in joint:
        joint[4] = joint[7]
    elif 4 not in joint and 7 not in joint:
        joint[4] = joint[7] = (0, 0)
        
    if 8 in joint and 11 not in joint:
        joint[11] = joint[8]
    elif 8 not in joint and 11 in joint:
        joint[8] = joint[11]
    elif 8 not in joint and 11 not in joint:
        joint[8] = joint[11] = (0, 0)
        
    if 9 in joint and 12 not in joint:
        joint[12] = joint[9]
    elif 9 not in joint and 12 in joint:
        joint[9] = joint[12]
    elif 9 not in joint and 12 not in joint:
        joint[9] = joint[12] = (0, 0)
        
    if 10 in joint and 13 not in joint:
        joint[13] = joint[10]
    elif 10 not in joint and 13 in joint:
        joint[10] = joint[13]
    elif 10 not in joint and 13 not in joint:
        joint[10] = joint[13] = (0, 0)
    
    if 14 in joint and 15 not in joint:
        joint[15] = joint[14]
    elif 14 not in joint and 15 in joint:
        joint[14] = joint[15]
    elif 14 not in joint and 15 not in joint:
        joint[14] = joint[15] = (0, 0)
        
    if 16 in joint and 17 not in joint:
        joint[17] = joint[16]
    elif 16 not in joint and 17 in joint:
        joint[16] = joint[17]
    elif 16 not in joint and 17 not in joint:
        joint[16] = joint[17] = (0, 0)
        
    return joint


def joint_filter(joint):
    if 9 not in joint and 12 not in joint and 10 not in joint and 13 not in joint:
        return False
    
    if 3 not in joint and 6 not in joint and 2 not in joint and 5 not in joint:
        return False
    
    
#    if 2 not in joint and 5 not in joint:
#        return False
#    
#    if 3 not in joint and 6 not in joint:
#        return False
#
#    if 4 not in joint and 7 not in joint:
#        return False
#
#    if 8 not in joint and 11 not in joint:
#        return False
#
#    if 14 not in joint and 15 not in joint:
#        return False
#
#    if 16 not in joint and 17 not in joint:
#        return False    
#
    if 9 not in joint and 12 not in joint:
        return False

    if 10 not in joint and 13 not in joint:
        return False
    
    return True
