def FOLDER(disabled: bool):
    a = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAC4jAAAuIwF4pT92AAAGMWlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNy4xLWMwMDAgNzkuYjBmOGJlOSwgMjAyMS8xMi8wOC0xOToxMToyMiAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iIHhtbG5zOnBob3Rvc2hvcD0iaHR0cDovL25zLmFkb2JlLmNvbS9waG90b3Nob3AvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VFdmVudCMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIDIzLjIgKFdpbmRvd3MpIiB4bXA6Q3JlYXRlRGF0ZT0iMjAyMi0wNS0xNFQxNTo0OTozMi0wMzowMCIgeG1wOk1vZGlmeURhdGU9IjIwMjItMDUtMjFUMTg6Mjg6MjUtMDM6MDAiIHhtcDpNZXRhZGF0YURhdGU9IjIwMjItMDUtMjFUMTg6Mjg6MjUtMDM6MDAiIGRjOmZvcm1hdD0iaW1hZ2UvcG5nIiBwaG90b3Nob3A6Q29sb3JNb2RlPSIzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjViNGNjMThiLTc3NGYtMDc0YS1iN2RlLWYxNTMwN2MwNzg2YSIgeG1wTU06RG9jdW1lbnRJRD0iYWRvYmU6ZG9jaWQ6cGhvdG9zaG9wOmNmYWNiOGRlLWQwNTgtN2U0Ni05NTRjLTU0MGJlNTg0NmUwZCIgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ4bXAuZGlkOmFlMGNmYmYwLWYwYWMtNmQ0OS05NDg0LTA2NTZjNTZjZjA4ZCI+IDx4bXBNTTpIaXN0b3J5PiA8cmRmOlNlcT4gPHJkZjpsaSBzdEV2dDphY3Rpb249ImNyZWF0ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6YWUwY2ZiZjAtZjBhYy02ZDQ5LTk0ODQtMDY1NmM1NmNmMDhkIiBzdEV2dDp3aGVuPSIyMDIyLTA1LTE0VDE1OjQ5OjMyLTAzOjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgMjMuMiAoV2luZG93cykiLz4gPHJkZjpsaSBzdEV2dDphY3Rpb249ImNvbnZlcnRlZCIgc3RFdnQ6cGFyYW1ldGVycz0iZnJvbSBhcHBsaWNhdGlvbi92bmQuYWRvYmUucGhvdG9zaG9wIHRvIGltYWdlL3BuZyIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6NWI0Y2MxOGItNzc0Zi0wNzRhLWI3ZGUtZjE1MzA3YzA3ODZhIiBzdEV2dDp3aGVuPSIyMDIyLTA1LTIxVDE4OjI4OjI1LTAzOjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgMjMuMiAoV2luZG93cykiIHN0RXZ0OmNoYW5nZWQ9Ii8iLz4gPC9yZGY6U2VxPiA8L3htcE1NOkhpc3Rvcnk+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+Q6OQQwAAATJJREFUWIXtlzFLw0AUx39pa4YiKOio0H6DDNJBO7STq36DQl2cit/ADyF0ku79Es0QHHTp4CqXwcHBaDvocFjjkJ6kIjS5i2a5Pzy4d+R/78e7BPKcOI4pU86PvJPDOwVmRYF4gADiHPEK9IoCyFs8HQ2TwjWStieH1Cq47eZa0+fzGx/3TyodABcmAN9y2012JudrTfImJDq6UulJYQBZ5R42qO5tsXicQ9K9HhBmtE9JvbxaAACbl8fMz8YqHeW0+8ApMKvoAtT7LTYO9nXtHWACBh0A2L0b8H59iwwEi/Alk0f6D2rpAZ4RACSdqPdbmZ+PusM0xLb2FRQlC2ABLIAFsAAWwAKs/A/IQBB1h39aUAbi132TuUA3Vki8f4YQy5pGs6GJfLVwyp6OS/8KvgAhmZPH/EsqtQAAAABJRU5ErkJggg=='
    b = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAC4jAAAuIwF4pT92AAAGMWlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNy4xLWMwMDAgNzkuYjBmOGJlOSwgMjAyMS8xMi8wOC0xOToxMToyMiAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iIHhtbG5zOnBob3Rvc2hvcD0iaHR0cDovL25zLmFkb2JlLmNvbS9waG90b3Nob3AvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VFdmVudCMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIDIzLjIgKFdpbmRvd3MpIiB4bXA6Q3JlYXRlRGF0ZT0iMjAyMi0wNS0xNFQxNTo0OTozMi0wMzowMCIgeG1wOk1vZGlmeURhdGU9IjIwMjItMDUtMjFUMTc6MjM6MDUtMDM6MDAiIHhtcDpNZXRhZGF0YURhdGU9IjIwMjItMDUtMjFUMTc6MjM6MDUtMDM6MDAiIGRjOmZvcm1hdD0iaW1hZ2UvcG5nIiBwaG90b3Nob3A6Q29sb3JNb2RlPSIzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjczNmQ3MDQyLWVjZTMtOTM0MC1iNmI5LTY2OWM0Y2QyNDE4MiIgeG1wTU06RG9jdW1lbnRJRD0iYWRvYmU6ZG9jaWQ6cGhvdG9zaG9wOjc4MGRjYmI4LTgzYmUtOTQ0NC1hMDBjLWUzNjY4ZDcxNjhmNiIgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ4bXAuZGlkOjhhZWE2NDk0LTIzMmMtMjE0Zi1iNGRhLWVmN2I3MmU5Zjk1MyI+IDx4bXBNTTpIaXN0b3J5PiA8cmRmOlNlcT4gPHJkZjpsaSBzdEV2dDphY3Rpb249ImNyZWF0ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6OGFlYTY0OTQtMjMyYy0yMTRmLWI0ZGEtZWY3YjcyZTlmOTUzIiBzdEV2dDp3aGVuPSIyMDIyLTA1LTE0VDE1OjQ5OjMyLTAzOjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgMjMuMiAoV2luZG93cykiLz4gPHJkZjpsaSBzdEV2dDphY3Rpb249ImNvbnZlcnRlZCIgc3RFdnQ6cGFyYW1ldGVycz0iZnJvbSBhcHBsaWNhdGlvbi92bmQuYWRvYmUucGhvdG9zaG9wIHRvIGltYWdlL3BuZyIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6NzM2ZDcwNDItZWNlMy05MzQwLWI2YjktNjY5YzRjZDI0MTgyIiBzdEV2dDp3aGVuPSIyMDIyLTA1LTIxVDE3OjIzOjA1LTAzOjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgMjMuMiAoV2luZG93cykiIHN0RXZ0OmNoYW5nZWQ9Ii8iLz4gPC9yZGY6U2VxPiA8L3htcE1NOkhpc3Rvcnk+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+GbYbQgAAAaZJREFUWIXt189LFWEUxvHPXGbMMqIgokVdMFxIEWEl7Q0iXOnOVkHhTm5k0N0E0kqCQlsJuhCCcBn9B+KmRQujMCKioI0F/ZCISrgxLe6M3ILutRnyBs2BA+954Z3ny5zD+54TxHGsnVZqqzqChnUF5xGj1uJMJx5hHO/zQvRiOhH+U3+AnXkBbuNzRoAYV/KIhyijC3qP9pmYnvO99vsMBEHg+cpj1y+PpltncCsrQIAFjMCNuQVnh0daHvr29YtTB7vScB3H8TQLQJjlUOf2HY709VtZfgjbcB+rybqZReoFPo+ZzABw7eaMc6dPpmFP4pu1fhzAbOZ74PCxE6bu3LN33/6sn7iE8cx/AAYGhwwMDnn96oV3b1d1dDTPQBhFJioXPXuyTL3wy7kAUit39yh3by4DFypVV0c3Cn19y6/i2E9vT9z2t6AAKAAKgAKgAPgnAKI0WPuQu8Nuab9oRKGGGWCyOqZUKtm1e89fEf+09tFkdaxxqwbDWJS9Lc/qi4k2OISlLRRfSjQ3mtKX6r39G/VWvdlolsfCBOBuoin476fjH+f+qiGnKyBKAAAAAElFTkSuQmCC'
    return a if disabled else b