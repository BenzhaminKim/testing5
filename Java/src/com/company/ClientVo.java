package com.company;

import io.netty.channel.ChannelHandlerContext;

public class ClientVo {

	/** 시설물 IP **/
	private String clientAddress;
	
	private int clientPort;
	
	private String facilityId;
	
	private ChannelHandlerContext ctx;

	private byte seq;

	/**
	 * @return
	 */
	public String getClientAddress() {
		return clientAddress;
	}

	/**
	 * @param clientAddress - the clientAddress to set
	 */
	public void setClientAddress(String clientAddress) {
		this.clientAddress = clientAddress;
	}

	/**
	 * @return
	 */
	public ChannelHandlerContext getCtx() {
		return ctx;
	}

	/**
	 * @param ctx - the ctx to set
	 */
	public void setCtx(ChannelHandlerContext ctx) {
		this.ctx = ctx;
	}
	
	public int getClientPort() {
		return clientPort;
	}
	
	public void setClientPort(int clientPort) {
		this.clientPort = clientPort;
	}
	
	public String getFacilityId() {
		return facilityId;
	}
	
	public void setFacilityId(String facilityId) {
		this.facilityId = facilityId;
	}

	public byte getSeq() {
		return seq;
	}

	public void setSeq(byte seq) {
		this.seq = seq;
	}

}
