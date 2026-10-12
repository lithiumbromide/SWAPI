---
title: "eDApplication Class"
project: ""
interface: "eDApplication"
member: ""
kind: "class"
source: "emodeltoolkit/eDApplication/eDApplication_Class.htm"
---

# eDApplication Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Top-level class of the eModelToolkit. Creates and contains a scene.

#### Header file code

```vb
class eDApplication
{
public:

static eDOutcome Create( eDApplication *& application ); //Creates and initializes your application

static eDOutcome Destroy( eDApplication *& application ); //Destroys your application

eDOutcome Initialize( eDApplicationParams params ); //Initializes the data for serialization

eDOutcome CreateScene( eDScene *& scene ); //Creates a scene

eDOutcome CloseScene(); //Closes a scene

eDOutcome GetApplicationUtils( eDApplicationUtils *& utils ) const; //Gets the version of eModelToolkit data

};
```
