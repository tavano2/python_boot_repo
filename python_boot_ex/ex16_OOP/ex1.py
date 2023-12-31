
"""
객체 지향 프로그래밍에 대해 알아보자.

    객체 지향 프록그래밍은 왜 배워야할까?
    이유는 코드가 점점 더 복잡해지고, 많은 일을 처리하려 할  때
    모든 관계들을 끌고 나가고 있기 때문이다.
    어떤 함수가 한 변수를 바꾸고
    또 같은 함수가 다른 변수에 또 다른 일을 한다.

    어느 시점부터 코드의 로직이 얽히고 설키기 시작하고
    코드를 추적하기 굉장히 어려워진다.

    이런 프로그래밍을 절차 지향형 프로그래밍이라고 한다.
    특정한 일을 하는 절차나 함수들을 만들어 구성하기 때문이다.
    절차지향 프로그래밍은 프로그래밍의 초기 패러다임이다.

    복잡한 프로젝트를 코딩할 때도 간단한 관계를 유지하려면 어떻게 해야 할까?
    바로 객체지향 패러다임이 필요할 때다.

자율 주행 보조 자동차를 만든다고 생각해보자.

    커피머신과는 비교도 안될만큼 복잡한 프로젝트 일 것이다.
    하나하나 차근히 살펴보자. 자율 주행 보조 자동차란 무엇이고 자율 주행 자동차가 되려면 어떤 요소가 있어야 할까?
    카메라 모듈 : 도로에 무엇이 있는지 주시하고 무엇인지 인식해야 한다.
    차선감지 모듈 : 차선을 넘지 않았는지, 시동을 꺼야하는지, 주차해야 하는지 판단해야한다.
    네비게이션 모듈 : 사용자가 지시했을 때 어떤 지점으로 가고싶은지 알아내고 어떻게 가야하는지 차 스스로 판단해야한다.
    연료 모듈 : 연료가 떨어졌는지, 떨어졌을 때 어떻게 해야하는지 관리해야한다.

이 프로젝트를 처리할 팀을 이끌고 있다고 상상해보자.
    팀 내에 이 다양한 모듈을 각각 담당할 하위 팀들이 있다.
    이 크고 복잡한 과업으르 별개의 모듈로 나누어 우리가 모두 동시에 차를 개발할 수 있다.
    생산성을 크게 향상시키고 차를 위한 소프트웨어를 훨씬 빠르게 개발할 수 있다.
    그것에 더해 이 모듈들에 재사용성도 늘어난다.
    다음 프로젝트가 드론을 개발 하는 프로젝트일 때 재사용할 수 있는 모듈은 그대로 가져 쓰면 되기 때문이다.

즉 모듈별로 재사용할 수 있는 코드들을 작성하는 것이 객체지향의 기본 원칙이라 할 수 있다.

객체지향의 또 다른 개념을 알아보자. 레스토랑 하나를 운영한다고 생각하자.
    우선 안내원이 되어 손님을 자리로 안내해야 하고, 손님이 무엇을 주문하면 웨이트리스가 되어 음식을 가져다줘야 한다.
    물론 주문을 받으면 요리사가 되어 요리를 해야한다. 이를 혼자서 감당하기에는 너무 많은 노동력이 들어가며 비효율적이다.
    이를 각각 담당 분야가 있는 사람들을 고용하는건 어떨까?
    자기 분야에 전문적인 사람들로 말이다.

    내가 매니저 역할을 맡아 각각 담당자들에게 뭘 해야하는지 말할 수 있고 관리하기만 하면 된다.
    그리고 각 담당자들이 세부적인 일을 어떻게 하는지 신경쓰지 않아도 된다.

    이 같은 개념을 코딩에 적용하면, 코드 안에서 관계들을 간소화하고
    더 크고 복잡한 프로젝트로 확장할 수 있게 된다.
"""

