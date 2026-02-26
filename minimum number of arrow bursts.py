class Solution:
    def findMinArrowShots(self, points):
        # If no balloons
        if not points:
            return 0

        # Sort balloons by their ending position
        points.sort(key=lambda x: x[1])

        # At least one arrow is needed
        arrows = 1

        # Position where first arrow is shot
        last_end = points[0][1]

        # Traverse remaining balloons
        for start, end in points:
            # If balloon starts after last arrow position
            if start > last_end:
                arrows += 1
                last_end = end  # shoot new arrow

        return arrows