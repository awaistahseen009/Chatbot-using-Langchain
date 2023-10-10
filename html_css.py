css='''
<style>
.main{
    font-size=62.5%;
}
img {
    width: 6rem;
    height: 6rem;
    object-fit: cover;
    border-radius: 50%;
    border: 1px solid #ccc;
    margin-right: 0.6rem; 
    border: 5px solid #fff;
}
.user-card {
    display: flex;
    gap: 1rem;
    align-items: center;
    background: rgb(2,0,36);
    background: linear-gradient(90deg, rgba(2,0,36,1) 6%, rgba(12,149,165,1) 21%, rgba(14,101,112,1) 38%, rgba(60,104,112,1) 100%, rgba(0,212,255,1) 100%);
    color: #eee;
    border-radius: 1.2rem;
    padding: 1rem 2.5rem;
    font-size: 1.2rem;
    margin-top:1.2rem;
    border: 1px solid #fff;
}
.llm-card {
    display: flex;
    gap: 1rem;
    align-items: center;
    background: rgb(58,58,181);
    background: linear-gradient(90deg, rgba(58,58,181,1) 0%, rgba(117,7,7,1) 50%, rgba(163,137,99,1) 100%);
    color: #eee;
    border-radius: 1.2rem;
    padding: 1rem 2.4rem;
    font-size: 1.2rem;
    margin-top:1.2rem;
}
'''
user_html='''
<div class="user-card">
       <div class="image">
        <img src="https://img.freepik.com/premium-photo/cute-girl-with-red-cloth_807689-498.jpg" alt="user-image-here">
       </div>
        <div class="text">
            <p class="text-para">
                {{message}}
            </p>
        </div>
    </div>
'''
llm_html='''
<div class="llm-card">
        <div class="image">
         <img src="https://www.techrepublic.com/wp-content/uploads/2023/07/tr71123-ai-art.jpeg" alt="user-image-here">
        </div>
         <div class="text">
             <p class="text-para">
                 {{message}}
             </p>
         </div>
     </div>
'''
