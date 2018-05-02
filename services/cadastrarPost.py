from Models.Post import post

def cadastrarPost(PostId,ForumId,OwnerId,CreateDate,Message,Visible):
    post.append({"PostId":PostId, "ForumId":ForumId,"OwnerId":OwnerId,"CreateDate":CreateDate,"Message":Message,"Visible":Visible})
    return post