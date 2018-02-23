package atinjin

import (
	"fmt"

	"github.com/elastic/go-elasticsearch/client"
)

func main() {
	url := client.WithHost("https://localhost:9200")
	es, _ := client.New(url)

	res, _ := es.Info()
	fmt.Println(res)

	// es.Search(body)

	// resp, err := es.Search(body)

}
