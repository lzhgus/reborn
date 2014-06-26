//
//  DropitBehavior.h
//  Dropit
//
//  Created by reborn_lzh on 6/21/14.
//  Copyright (c) 2014 reborn_lzh. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface DropitBehavior : UIDynamicBehavior

-(void)addItem:(id <UIDynamicItem>)item;
-(void)removeItem:(id <UIDynamicItem>)item;
@end
