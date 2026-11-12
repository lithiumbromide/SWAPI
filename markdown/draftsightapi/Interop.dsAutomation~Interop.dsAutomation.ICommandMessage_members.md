---
title: "ICommandMessage Interface Members"
project: ""
interface: "ICommandMessage_members"
member: ""
kind: "members"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html"
---

# ICommandMessage Interface Members

The following tables list the members exposed by [ICommandMessage](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | PromptExplanation | Gets or sets the text for the prompt in the command window. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddTracker | Adds a tracker, the mechanism that replaces the cursor with a temporary entity when prompting a user for a value, keyword, or selection. |
| Method | GetLastError | Displays the status of the last-run command in the command window. |
| Method | GetLastUserInput | Gets the last value input by a user in the command window. |
| Method | PrintLine | Displays the specified string in the command window. |
| Method | PromptForAngle | Displays the specified prompt and default value for an angle in the command window and gets the angle input by the user. |
| Method | PromptForAngleOrKeyword | Obsolete. Superseded by ICommandMessage::PromptForAngleOrKeyword2 . |
| Method | PromptForAngleOrKeyword2 | Displays the specified prompt, local keywords, and default value for an angle in the command window and gets the user's input. |
| Method | PromptForBlockInsertion | Prompts the user for the insertion point, scale factors, and rotation angle to use when inserting a Block Instance . |
| Method | PromptForBool | Displays the specified prompt and default Boolean value in the command window and gets the Boolean input by the user. |
| Method | PromptForBoolOrKeyword | Displays the specified prompt, local keywords, and default value for the Boolean in the command window and gets the user's input. |
| Method | PromptForDistance | Displays the specified prompt and default value for the linear distance in the command window and gets the linear distance input by the user. |
| Method | PromptForDistanceOrKeyword | Obsolete. Superseded by ICommandMessage::PromptForDistanceOrKeyword2 . |
| Method | PromptForDistanceOrKeyword2 | Displays the specified prompt, local keywords, and default value for the linear distance in the command window and gets the user's input. |
| Method | PromptForDouble | Displays the specified prompt and default value for the double in the command window and gets the double input by the user. |
| Method | PromptForDoubleOrKeyword | Displays the specified prompt, local keywords, and default value for the double in the command window and gets the user's input. |
| Method | PromptForFileName | Displays the specified prompt in the command window and gets the file name input by the user. |
| Method | PromptForFileNameOrKeyword | Displays the specified prompt, local keywords, and default value for the file name in command window and gets the user's input. |
| Method | PromptForInteger | Displays the specified prompt and default value for the integer or long in the command window and gets the integer or long input by the user. |
| Method | PromptForIntegerOrKeyword | Displays the specified prompt, local keywords, and default value for the integer or long in the command window and gets the user's input. |
| Method | PromptForKeyword | Obsoleted. Superseded by ICommandMessage::PromptForKeyword2 . |
| Method | PromptForKeyword2 | Displays the specified prompt, local keywords, and default value for the keyword in the command window and gets the keyword input by the user. |
| Method | PromptForMouseOrKeyword | Obsolete. Superseded by ICommandMessage::PromptForMouseOrKeyword2 . |
| Method | PromptForMouseOrKeyword2 | Displays the specified prompt in the command window with the specified local keywords, base point, and default mouse click point. Returns the user's input either from the command window (keyword) or the mouse/keyboard (mouse click point, mouse event type, and keyboard modificators). |
| Method | PromptForOrientation | Displays the specified prompt and default value for the orientation in the command window and gets the orientation input by the user. |
| Method | PromptForOrientationOrKeyword | Obsolete. Superseded by ICommandMessage::PromptForOrientationOrKeyword2 . |
| Method | PromptForOrientationOrKeyword2 | Displays the specified prompt, local keywords, and default value for the orientation in the command window and gets the user's input. |
| Method | PromptForPoint | Obsolete. Superseded by ICommandMessage::PromptForPoint2 . |
| Method | PromptForPoint2 | Displays the specified prompt in the command window gets the x, y, and z coordinates specified by the user. |
| Method | PromptForPointOrKeyword | Displays the specified prompt, local keywords, and default value for the point in the command window and gets the user's input. |
| Method | PromptForSelection | Displays the specified prompt for selecting one or more entities. |
| Method | PromptForSelectionOrKeyword | Displays the specified prompt and local keywords for selecting one or more entities in the command window and gets the user's input. |
| Method | PromptForString | Displays the specified prompt and default value in the command window and gets the user's input. |
| Method | PromptForStringOrKeyword | Displays the specified prompt, local keywords, and default string in the command window and gets the user's input. |
| Method | RemoveTracker | Removes the tracker, the mechanism that draws temporary entities along the cursor's path when prompting a user for a value, keyword, or selection. |

[Top](#topBookmark)

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[ICommand Interface](Interop.dsAutomation~Interop.dsAutomation.ICommand.html)
