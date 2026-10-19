const MINUTE = 60
const HOUR = 60 * MINUTE
const DAY = 24 * HOUR

function plural(count: number, unit: string): string {
  return `${count} ${unit}${count === 1 ? "" : "s"} ago`
}

export function formatRelativeTime(date: Date | string): string {
  const then = typeof date === "string" ? new Date(date) : date
  if (Number.isNaN(then.getTime())) {
    return "Invalid date"
  }

  const seconds = (Date.now() - then.getTime()) / 1000
  if (seconds < MINUTE) {
    return "just now"
  }
  if (seconds < HOUR) {
    return plural(Math.floor(seconds / MINUTE), "minute")
  }
  if (seconds < DAY) {
    return plural(Math.floor(seconds / HOUR), "hour")
  }
  if (seconds < 30 * DAY) {
    return plural(Math.floor(seconds / DAY), "day")
  }
  return then.toLocaleDateString()
}
