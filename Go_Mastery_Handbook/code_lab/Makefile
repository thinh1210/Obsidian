GO = go
GOFLAGS = -v

GO_SRCS = 01_nil_interface_trap.go \
          02_slice_backing_and_fullslice.go \
          03_unsafe_zerocopy_and_layout.go \
          04_concurrency_patterns_context.go \
          05_defer_and_iota_tricks.go \
          06_sync_pool_and_atomic.go

TARGETS = $(GO_SRCS:.go=)

.PHONY: all run clean vet

all: $(TARGETS)

$(TARGETS): %: %.go
	$(GO) build -o $@ $<

vet:
	$(GO) vet ./...

run: all
	@echo "============================================================"
	@echo "    RUNNING ALL 6 GO ADVANCED MASTERY CODE LAB SUITES"
	@echo "============================================================"
	@for target in $(TARGETS); do \
		echo ""; \
		./$$target; \
	done

clean:
	rm -f $(TARGETS)
