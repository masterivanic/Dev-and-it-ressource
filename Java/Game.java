/*
* To change this license header, choose License Headers in Project Properties.
* To change this template file, choose Tools | Templates
* and open the template in the editor.
*/
package com.company.pages.de_game;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.WindowConstants;

public class Game extends JPanel {

    private final int WIDTH = 50;
    private Deque<SnakePart> snake = new ArrayDeque<>();
    private int offSet = 0;
    private int newDirection = 39;
    private Random rand = new Random();
    private Point apple = new Point(0, 0);
    private boolean isGrowing = false;
    private boolean gameLost = false;

    public static void main(String[] args) {
        JFrame laFenetre = new JFrame("JEU DE SERPENT");
        Game panel = new Game();
        laFenetre.addKeyListener(new KeyListener() {
            @Override
            public void keyTyped(KeyEvent arg0) throws UnsupportedOperationException {
                System.out.println(arg0);
            }

            @Override
            public void keyPressed(KeyEvent e) throws UnsupportedOperationException {
                panel.onKeyPressed(e.getKeyCode());
            }

            @Override
            public void keyReleased(KeyEvent arg0) throws UnsupportedOperationException {
                System.out.println(arg0);
            }
        });

        laFenetre.setContentPane(panel);
        laFenetre.setResizable(false);
        laFenetre.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        laFenetre.setSize(13 * 50, 13 * 50);
        laFenetre.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        laFenetre.setVisible(true);
    }

    public Game() {
        snake.add(new SnakePart(0, 0, 39));
        setBackground(Color.WHITE);
        new Thread(new Runnable() {
            @Override
            public void run() {
                while (true) {
                    repaint();
                    try {
                        Thread.sleep(1000 / 60);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        }).start();
    }

    public void createApple() {
        boolean positionAvailable = false;
        do {
            apple.y = rand.nextInt(12);
            apple.x = rand.nextInt(12);
            positionAvailable = true;
            for (SnakePart p : snake) {
                if (p.x == apple.x && p.y == apple.y) {
                    positionAvailable = false;
                    break;
                }
            }
        } while (!positionAvailable);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        if (gameLost) {
            g.setColor(Color.RED);
            g.setFont(new Font("Arial", 90, 90));
            g.drawString("Partie terminée", 20, 13 * 50 / 2);
            return;
        }

        offSet += 5;
        SnakePart head = null;
        if (offSet == WIDTH) {
            offSet = 0;
            try {
                head = (SnakePart) snake.getFirst().clone();
                head.move();
                head.direction = newDirection;
                snake.addFirst(head);

                if (head.x == apple.x && head.y == apple.y) {
                    isGrowing = true;
                    createApple();
                }

                if (!isGrowing) {
                    snake.pollLast();
                } else {
                    isGrowing = false;
                }

            } catch (CloneNotSupportedException ex) {
                Logger.getLogger(Game.class.getName()).log(Level.SEVERE, null, ex);
            }
        }

        g.setColor(Color.RED);
        g.fillOval(apple.x * WIDTH + WIDTH / 4, apple.y * WIDTH + WIDTH / 4, WIDTH / 2, WIDTH / 2);

        g.setColor(Color.DARK_GRAY);
        for (SnakePart p : snake) {
            if (offSet == 0) {
                if (p != head) {
                    if (p.x == head.x && p.y == head.y) {
                        gameLost = true;
                        System.err.println("Partie perdue");
                        // System.exit(0);
                    }
                }
            }
            if (p.direction == 37 || p.direction == 39) {
                g.fillRect(p.x * WIDTH + ((p.direction == 37) ? -offSet : offSet), p.y * WIDTH, WIDTH, WIDTH);
            } else {
                g.fillRect(p.x * WIDTH, p.y * WIDTH + ((p.direction == 39) ? -offSet : offSet), WIDTH, WIDTH);
            }
        }

        g.setColor(Color.BLUE);
        g.drawString("Score " + (snake.size() - 1), 10, 20);
    }

    public void onKeyPressed(int keyCode) throws UnsupportedOperationException {
        if (keyCode >= 37 && keyCode <= 40) {
            if (Math.abs(keyCode - newDirection) != 2) {
                newDirection = keyCode;
            }
        }
    }

    class SnakePart {

        public int x, y, direction;

        public SnakePart(int x, int y, int direction) {
            this.x = x;
            this.y = y;
            this.direction = direction;
        }

        public void move() {
            if (direction == 37 || direction == 39) {
                x += (direction == 37) ? -1 : 1;
                if (x > 13) {
                    x = -1;
                } else if (x < -1) {
                    x = 13;
                }
            } else {
                y += (direction == 38) ? -1 : 1;
                if (y > 13) {
                    y = -1;
                } else if (y < -1) {
                    y = 13;
                }
            }
        }

        @Override
        protected Object clone() throws CloneNotSupportedException {
            return new SnakePart(x, y, direction);
        }
    }

}
