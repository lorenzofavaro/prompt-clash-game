cd admin_interface
docker build -t registry.example.com/theme-prompt-clash/admin-interface:latest .
docker push registry.example.com/theme-prompt-clash/admin-interface:latest
cd ../admin_service
docker build -t registry.example.com/theme-prompt-clash/admin-service:latest .
docker push registry.example.com/theme-prompt-clash/admin-service:latest
cd ../chat_service
docker build -t registry.example.com/theme-prompt-clash/chat-service:latest .
docker push registry.example.com/theme-prompt-clash/chat-service:latest
cd ../round_manager_service
docker build -t registry.example.com/theme-prompt-clash/round-manager-service:latest .
docker push registry.example.com/theme-prompt-clash/round-manager-service:latest
cd ../user_interface
docker build -t registry.example.com/theme-prompt-clash/user-interface:latest .
docker push registry.example.com/theme-prompt-clash/user-interface:latest
