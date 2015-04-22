def intersection_point(self, other):
    first = (self.first.x - self.second.x) * (other.second.y - self.third.y) - (self.first.y - self.second.y) * (other.second.x - other.first.x)
    second = (self.first.x - other.first.x) * (other.second.y - self.third.y) - (self.first.y - other.first.y) * (other.second.x - other.first.x)
    third = (self.first.x - self.second.x) * (self.first.y - self.third.y) - (self.first.y - self.second.y) * (self.first.x - other.first.x)

    first_relation = second / first
    second_relation = third / first
 
    if (first_relation >= 0 and first_relation <= 1 and second_relation >= 0 and second_relation <= 1):
        x = self.first.x  + first_relation * (self.second.x - self.first.x)
        y = self.first.y + first_relation * (self.second.y - self.first.y)
    return Point(x, y);
	
 
	
