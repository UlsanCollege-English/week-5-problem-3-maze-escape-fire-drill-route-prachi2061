def find_path(grid, start, end):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        return None
    if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        return None
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None
    visited = [[False] * cols for _ in range(rows)]
    def dfs(r, c, path):
        if (r, c) == end:
            return path + [(r, c)]
        visited[r][c] = True
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and not visited[nr][nc]:
                res = dfs(nr, nc, path + [(r, c)])
                if res:
                    return res
        return None
    return dfs(start[0], start[1], [])
