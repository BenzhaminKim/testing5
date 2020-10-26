package com.company;

import io.netty.channel.ChannelHandlerContext;

import java.util.ArrayList;
import java.util.List;

public class ClientList {
	
	static List<ClientVo> clientVoList = new ArrayList<ClientVo>();

	/**
	 * 클라이언트 IP 저장 여부 확인
	 *
	 * @param obeId
	 * @return
	 */
	public static boolean isSavedClientInfo(String clientAddress, int port) {

		for (int i = 0; i < clientVoList.size(); i++) {
			ClientVo clientVo = clientVoList.get(i);

			// ADDRESS를 비교하여 같으면 이미 저장되어있기 때문에 true 반환
			if (clientVo.getClientAddress().compareTo(clientAddress) == 0) {
				if (clientVo.getClientPort() == port) {
					return true;
				}
			}
		}

		return false;
	}
	
	/**
	 * ctx로 저장여부 확인
	 *
	 * @param ctx
	 * @return
	 */
	public static boolean isSavedClientInfo(ChannelHandlerContext ctx) {

		for (int i = 0; i < clientVoList.size(); i++) {
			ClientVo clientVo = clientVoList.get(i);

			// OBE ID를 비교하여 같으면 이미 저장되어있기 때문에 true 반환
			if (clientVo.getCtx() == ctx) {
				return true;
			}
		}

		return false;
	}
	
	/**
	 * 시설물 세션 저장
	 *
	 * @param clientAddress
	 * @param ctx
	 */
	public static void addClientInfo(String clientAddress, ChannelHandlerContext ctx, int port) {

		ClientVo clientVo = new ClientVo();

		// 버스 ID
		clientVo.setClientAddress(clientAddress);
		// 세션
		clientVo.setCtx(ctx);

		clientVo.setClientPort(port);
		
		// Obe Info 추가
		clientVoList.add(clientVo);

	}
	
	/**
	 * 차량단말기 ID로 ObeInfo객체 반환
	 *
	 * @param obeId
	 * @return
	 */
	public static ClientVo getClientVo(String clientAddress, int port) {
		for (int i = 0; i < clientVoList.size(); i++) {
			ClientVo clientVo = clientVoList.get(i);

			// OBE ID를 비교하여 같으면 Obe Info 반환
			if (clientVo.getClientAddress().trim().compareTo(clientAddress.trim()) == 0 && clientVo.getClientPort() == port) {
				return clientVo;
			}
		}
		
		return null;
	}
	
	/**
	 * 세션정보로 Client객체 반환
	 *
	 * @param busId
	 * @return
	 */
	public static ClientVo getClientVo(ChannelHandlerContext ctx) {
		for (int i = 0; i < clientVoList.size(); i++) {
			ClientVo clientVo = clientVoList.get(i);

			// 세션을 비교하여 같으면 client Info 반환
			if (clientVo.getCtx() == ctx) {
				return clientVo;
			}
		}
		
		return null;
	}
	
	/**
	 * 세션정보 제거
	 *
	 * @param ctx
	 */
	public static void removeClientInfo(ChannelHandlerContext ctx) {
		for (int i = 0; i < clientVoList.size(); i++) {
			ClientVo clientVo = clientVoList.get(i);

			// 세션정보를 비교하여 같으면 Client Info 삭제
			if (clientVo.getCtx() == ctx) {
				clientVoList.remove(i);
				break;
			}
		}
		
	}

}
