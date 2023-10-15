//run with command:
//gcc -o Server.exe Server.c -lWs2_32

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <winsock2.h>

//ascii values of M (77) and S (83):
#define PORT 7783

#define STRING_SIZE 150

int main(int argc, char** argv)
{
    WSADATA wsa;
    SOCKET sock, new_socket;
    struct sockaddr_in server, client;
    int exitCode = EXIT_SUCCESS, c, requestSize;
    bool wsaInitialized = false, socketCreated = false;
    char clientRequest[STRING_SIZE];

    printf("Initialising Winsock...\n");
    if(WSAStartup(MAKEWORD(2, 2), &wsa) != 0) {
        printf("Error %d", WSAGetLastError());
        exitCode = EXIT_FAILURE;
        goto defer;
    }
    wsaInitialized = true;
    printf("Winsock Initialised.\n");

    if((sock = socket(AF_INET, SOCK_STREAM, 0)) == INVALID_SOCKET) {
        printf("Socket creation failed: %d", WSAGetLastError());
        exitCode = EXIT_FAILURE;
        goto defer;
    }
    printf("Socket created.\n");
    socketCreated = true;

    server.sin_family = AF_INET;
	server.sin_addr.s_addr = INADDR_ANY;
	server.sin_port = htons(PORT);
    if(bind(sock, (struct sockaddr*)&server, sizeof(server)) == SOCKET_ERROR) {
        printf("Bind failed: %d", WSAGetLastError());
        exitCode = EXIT_FAILURE;
        goto defer;
    }
    printf("Binding complete.\n");

    listen(sock, 1);

    c = sizeof(struct sockaddr_in);
    new_socket = accept(sock, (struct sockaddr*)&client, &c);
    if(new_socket == INVALID_SOCKET) {
        printf("Accepting client failed: %d", WSAGetLastError());
        exitCode = EXIT_FAILURE;
        goto defer;
    }
    printf("Client connected.\n");

    if((requestSize = recv(new_socket, clientRequest, STRING_SIZE, 0)) == SOCKET_ERROR)
        perror("recv failed\n");

    clientRequest[requestSize] = '\0';
    puts(clientRequest);

defer:
    if(wsaInitialized) WSACleanup();
    if(socketCreated) closesocket(sock);
    return exitCode;
}