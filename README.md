    if state != "running":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # יציאה בלחיצה על Esc
                    pygame.quit()
                    sys.exit()
