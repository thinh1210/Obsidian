RUSTC := $(shell which rustc 2>/dev/null || echo $(HOME)/.cargo/bin/rustc)
RUSTFLAGS = -C opt-level=2 --edition=2021 -D warnings

RS_SRCS = 01_memory_layout_and_niche.rs \
          02_ownership_and_interior_mutability.rs \
          03_repr_packed_and_volatile.rs \
          04_fat_pointers_and_dispatch.rs \
          05_maybe_uninit_and_unsafe_ffi.rs \
          06_fearless_concurrency_atomics.rs

TARGETS = $(RS_SRCS:.rs=)

.PHONY: all clean run

all: $(TARGETS)

$(TARGETS): %: %.rs
	$(RUSTC) $(RUSTFLAGS) $< -o $@

run: all
	@echo "============================================================"
	@echo "    RUNNING ALL 6 RUST ADVANCED CODE LAB TEST SUITES"
	@echo "============================================================"
	@for target in $(TARGETS); do \
		echo ""; \
		./$$target; \
	done

clean:
	rm -f $(TARGETS)
