//
//  DropitBehavior.m
//  Dropit
//
//  Created by reborn_lzh on 6/21/14.
//  Copyright (c) 2014 reborn_lzh. All rights reserved.
//

#import "DropitBehavior.h"
@interface DropitBehavior()
@property (strong, nonatomic) UIGravityBehavior *gravity;
@property (strong, nonatomic) UICollisionBehavior *collider;
@end

@implementation DropitBehavior


-(UIGravityBehavior *)gravity
{
    if(!_gravity){
        _gravity = [[UIGravityBehavior alloc] init];
        _gravity.magnitude = 0.9;
   //     [self.animator addBehavior:_gravity];
    }
    return _gravity;
}

-(UICollisionBehavior *)collider
{
    if (!_collider) {
        _collider = [[UICollisionBehavior alloc]init];
        _collider.translatesReferenceBoundsIntoBoundary = YES;
     //   [self.animator addBehavior:_collider];
    }
    return _collider;
}

-(void)addItem:(id <UIDynamicItem>)item
{
    [self.gravity addItem:item];
    [self.collider addItem:item];
}
-(void)removeItem:(id <UIDynamicItem>)item;
{
    [self.gravity removeItem:item];
    [self.collider removeItem:item];
}


-(instancetype)init
{
    self = [super init];
    [self addChildBehavior:self.gravity];
    [self addChildBehavior:self.collider];
    return self; // uidynamicItem 的初始化方法
}

@end
