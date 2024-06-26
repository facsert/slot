package main

import (
	"fmt"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/log"
	// "github.com/gofiber/swagger"

	"slot/lib/comm"
	// _ "slot/lib/database"
	// _ "slot/utils/router"
	// _ "slot/middleware"
	// _ "slot/docs"
)

func init() {
	comm.Init()
    // database.Init()
	
}

const (
	host     = "localhost"
	port     = 8050
)

// @title Fiber API
// @version 1.0.0
// @host localhost:8050
// @BasePath /api/v1
func main() {
	app := fiber.New()
    
    // middleware.Init(app)
	// router.Init(app)

	// app.Get("/*", swagger.HandlerDefault)
	
	log.Fatal(app.Listen(fmt.Sprintf("%v:%v", host, port)))
}
