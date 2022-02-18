def solution(scriptByExtension):
    return sorted([[y,x] for x,y in scriptByExtension.items()])
	
"""
Example

For

scriptByExtension = {
  "validate": "py",
  "getLimits": "md",
  "generateOutputs": "json"
}
the output should be

solution(scriptByExtension) = [["json", "generateOutputs"], 
                                          ["md", "getLimits"], 
                                          ["py", "validate"]]
"""