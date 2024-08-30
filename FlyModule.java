package com.example.myhackclient.modules;

import net.minecraft.client.Minecraft;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;

public class FlyModule {

    private final Minecraft mc = Minecraft.getInstance();

    @SubscribeEvent
    public void onClientTick(TickEvent.ClientTickEvent event) {
        if (mc.player != null && mc.player.isAlive()) {
            mc.player.abilities.isFlying = true;
        }
    }
}
