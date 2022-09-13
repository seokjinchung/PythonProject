import pygame
import sys

pygame.init()
pygame.display.set_caption('Jumping dog')
Screen_width = 750
Screen_height = 400


def main():
    
    # 스크린, fps 설정
    screen = pygame.display.set_mode((Screen_width, Screen_height))
    background = pygame.image.load("backpic.jpg")
    fps = pygame.time.Clock()

    # 개이미지와 초기위치설정
    dog = pygame.image.load('dog.png')
    dog_height = dog.get_size()[1]
    dog_x = 50
    dog_y = Screen_height - dog_height
    is_on_bottom = True #초기위치 땅
    is_jumped = False #점프한 상태 아님

    #  나무 이미지와 초기위치 설정
    tree = pygame.image.load('tree.png')
    tree_height = tree.get_size()[1]
    tree_x = Screen_width
    tree_y = Screen_height - tree_height

    # 점수설정
    point = 0
    font_point = pygame.font.SysFont(None,30)
    
    running = True

    #게임이 진행중인동안 
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
 
            elif event.type == pygame.KEYDOWN: #키 눌러서 점프하면 점프에 True값
                if is_on_bottom:   #키 눌렀을때 땅에 있으면 점프 가능, 공중에 떠있으면 점프 불가능
                    is_jumped = True
                    is_on_bottom = False

 
        if is_jumped:
            dog_y -= 10.0 #점프중 개의 y축위치 증가
        elif not is_jumped and not is_on_bottom:  #꼭대기에 있을때 
            dog_y += 10.0 #떨어지는중 개의 y축위치 감소

      
        if is_jumped and dog_y <= 150:
            is_jumped = False #개가 스크린 높이 150에 도달하면 떨어지게

        if not is_on_bottom and dog_y >= Screen_height - dog_height: #개가 스크린 아래를 벗어낫을때 
            is_on_bottom = True  
            dog_y = Screen_height - dog_height # 스크린 아래로 벗어나면 땅에 있게 조정
 
        # 나무 움직임
        tree_x -= 12.0

        if tree_x <= 0:
            tree_x = Screen_width #스크린 밖으로 나가면 다시 제자리로
            point += 1

        x_mod = (point//2)
        tree_x -= x_mod*2  #2점 오를때마다 가속

        #충돌처리
        dog_rect = dog.get_rect()
        dog_rect.left = dog_x
        dog_rect.top = dog_y

        tree_rect = tree.get_rect()
        tree_rect.left = tree_x
        tree_rect.top = tree_y

        if dog_rect.colliderect(tree_rect):
            print("충돌")
            running = False        

        # 캐릭터, 배경, 점수 추가
        screen.blit(background, (0,0))
        screen.blit(dog, (dog_x, dog_y))
        screen.blit(tree, (tree_x, tree_y))

        text_point = font_point.render(str(point),True,(0,0,0))
        screen.blit(text_point,(10,10))

        # 디스플레이 업데이트해서 출력
        pygame.display.update()
        fps.tick(30)


if __name__ == '__main__':
    main()