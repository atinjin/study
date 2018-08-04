pragma solidity ^0.4.21;

contract SellAndBuy {
    uint public value;      //상품의 가격
    address public seller;  //판매자
    address public buyer;   //구매자
    enum State { Created, Locked, Inactive }    //계약의 상태 종류
    State public state;     //계약 상태

    // `msg.value`는 짝수여야 한다.
    // 솔리디티에서는 정수형을 나눌 경우 소수점을 버리기 때문이다.
    // 짝수였는지 확인하는 코드를 넣는다.
    function Purchase() public payable {
        seller = msg.sender;    //계약을 만드는 사람이 판매자이다.
        value = msg.value / 2;  //판매자는 상품 가격의 2배되는 이더를 deposit으로 내놓는다.
        require((2 * value) == msg.value, "");
    }

    modifier condition(bool _condition) {
        require(_condition, "");
        _;
    }

    modifier onlyBuyer() {
        require(msg.sender == buyer, "");
        _;
    }

    modifier onlySeller() {
        require(msg.sender == seller, "");
        _;
    }

    modifier inState(State _state) {
        require(state == _state, "계약 상태가 맞지 않습니다. "+state);
        _;
    }

    event Aborted();
    event PurchaseConfirmed();
    event ItemReceived();

    /// 계약 취소
    /// Created 상태인 경우만 취소 가능하다.
    
    function abort()
        public
        onlySeller
        inState(State.Created)
    {
        emit Aborted();
        state = State.Inactive;     // 계약 상태는 "파기" 상태로 돌려 계약을 못하게 한다.
        seller.transfer(address(this).balance);  // 판매자에게 deposit을 되돌려 준다.
    }

    /// 구매자는 구매 확인으로 계약을 시작한다.
    /// 구매자도 판매 가격에 deposit을 포함해서 2배되는 이더를 가지고 들어온다. `2 * value` ether.
    function confirmPurchase()
        public
        inState(State.Created)
        condition(msg.value == (2 * value))
        payable
    {
        emit PurchaseConfirmed();
        buyer = msg.sender;     // 메시지를 보낸 사람은 구매자이다.
        state = State.Locked;   // 계약 상태는 "잠금" 상태가 된다.
    }

    /// 구매자는 상품을 받았을 경우, 확인 메시지를 보낸다.
    function confirmReceived()
        public
        onlyBuyer
        inState(State.Locked)   // "잠김" 상태에서 구매자만 보낼 수 있다.
    {
        emit ItemReceived();
        state = State.Inactive; // 현재 계약은 완료되어 "파기" 상태가 된다.

        // NOTE: This actually allows both the buyer and the seller to
        // block the refund - the withdraw pattern should be used.

        buyer.transfer(value);  // 계약이 완료되었기 때문에 판매자는 deposit을 돌려받는다.
        seller.transfer(address(this).balance);  // 판매자는 자신이 건 deposit을 포함한 판매자가 지불한 상품값까지 모두 받는다.
    }
}