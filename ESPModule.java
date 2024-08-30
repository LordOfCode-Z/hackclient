package com.example.myhackclient.modules;

import net.minecraft.client.Minecraft;
import net.minecraft.client.renderer.entity.RenderManager;
import net.minecraft.entity.Entity;
import net.minecraft.entity.player.PlayerEntity;
import net.minecraftforge.client.event.RenderWorldLastEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;

import java.awt.*;

public class ESPModule {

    private final Minecraft mc = Minecraft.getInstance();

    @SubscribeEvent
    public void onRenderWorldLast(RenderWorldLastEvent event) {
        for (Entity entity : mc.world.getAllEntities()) {
            if (entity instanceof PlayerEntity && entity != mc.player) {
                drawESPBox((PlayerEntity) entity);
            }
        }
    }

    private void drawESPBox(PlayerEntity player) {
        RenderManager renderManager = mc.getRenderManager();
        double x = player.getPosX() - renderManager.info.getProjectedView().x;
        double y = player.getPosY() - renderManager.info.getProjectedView().y;
        double z = player.getPosZ() - renderManager.info.getProjectedView().z;
        
        // Bu örnekte basit bir kırmızı kutu çizeceğiz
        renderManager.renderBoundingBox(player.getBoundingBox().offset(-x, -y, -z), Color.RED.getRGB());
    }
}
