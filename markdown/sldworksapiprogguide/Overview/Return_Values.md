---
title: "Return Values"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Return_Values.htm"
---

# Return Values

If you are using unmanaged C++ COM, the SOLIDWORKS API function always returns an HRESULT. Any additional return values should be passed by reference as arguments.

SOLIDWORKS uses HRESULT return values to indicate that the code was called successfully. It is not meant as an indication that your call achieved its objective. For example, calling [IBody2::IGetFirstFace](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstFace.html) will have an HRESULT return value of S_OK if the code for IBody2::IGetFirstFace was called successfully. It does not mean that the code succeeded in finding the first face. In this case, you should check the LPFACE2 return value for a NULL condition.

### Object Return Values

If an API method returns an object, it is always a good idea to verify that the object returned is not NULL. This type of error checking is good programming practice and avoids crashes in your code for unexpected conditions. For example:

```vb
// In unmanaged C++ (COM)
LPFACE m_Face = NULL;
HRESULT hres = m_PartDoc->IBodyObject(&m_Body); // Get body object from the part
if (m_Body == NULL) return;

hres = m_Body->IGetFirstFace(&m_Face);  // Get first face object from the body
while (m_Face != NULL)     // While faces exist, traverse them
{
double theFaceArea = 0.0;
hres = m_Face->GetArea(&theFaceArea);  // Sample use of face object pointer

LPENTITY m_Entity = NULL;    // Obtain pointer to Entity object
hres = m_Face->QueryInterface( IID_IEntity, (LPVOID*)&m_Entity);
if (m_Entity != NULL)
{
VARIANT_BOOL boolres = FALSE;
hres = m_Entity->Select(TRUE,&boolres); // Sample use of entity object pointer
m_Entity->Release();    // Release Entity object pointer
}

LPFACE pnextFace = NULL;
m_Face->IGetNextFace(&pnextFace);   // Get the next face object
m_Face->Release();     // Release previous object pointer
m_Face= pnextFace;
}        // End while faces exist

m_PartDoc->Release();     // Release all pointers when done
m_Body->Release();     // Good idea to check for NULL if not certain

// In unmanaged C++ (Dispatch)
LPDISPATCH bodyDisp = m_PartDoc.Body();  // Get body object from the part
if (bodyDisp == NULL) return;
IBody m_Body(bodyDisp);

LPDISPATCH faceDisp = m_Body.GetFirstFace(); // Get Dispatch pointer to first face
while (faceDisp)      // While faces exist, traverse them
{
IFace m_Face(faceDisp);    // Get the Face member
double theFaceArea = m_Face.GetArea();  // Sample use of face object pointer

IEntity m_Entity(faceDisp);    // Obtain pointer to entity object
faceDisp->AddRef();     // Manually increment the reference count

boolean retval = m_Entity.Select(TRUE);   // Sample use of entity object pointer

faceDisp = m_Face.GetNextFace();   // Get the next face

}      // End while faces exist
      // Objects go out of scope and ref count decremented in destructor

' In Visual Basic for Applications (VBA)
Dim FaceObj,BodyObj As Object
Dim theFaceArea As Double
Dim ok As Boolean

Set BodyObj = PartObj.Body   ' Get body object from the part
' PartObj represents PartDoc interface - possibly obtained
' using ActiveDoc, OpenDoc, NewPart, etc. functions
If (BodyObj Is Nothing) Then
swApp.SendMsgToUser "Error! Part has no body."
Exit Sub
End If

Set FaceObj = BodyObj.GetFirstFace  ' Get first face from the body object
While Not FaceObj Is Nothing   ' While faces exist, traverse them

theFaceArea = FaceObj.GetArea  ' Sample use of face object pointer

ok = FaceObj.Select(True)   ' Sample use of entity object pointer
' Face object can be used for entity object calls
Set FaceObj = FaceObj.GetNextFace ' Get the next face

Wend      ' End while faces exist

Set BodyObj = Nothing   ' Clean up variables
Set FaceObj = Nothing
Set PartObj = Nothing
```

### VARIANT Return Values

SOLIDWORKS might also return an empty or NULL VARIANT. It is also good programming practice to check for this condition. The following unmanaged C++ and VBA examples show you one method of checking for an empty VARIANT:

```vb
// In unmanaged C++
VARIANT v = m_ModelDoc.GetMassProperties();  // Get the mass properties
If ((v.vt == VT_EMPTY) || (V_VT(&v) == VT_NULL)) // Error occurred
return;

' In Visual Basic for Applications (VBA)
PickPt = m_SelectionManager.GetSelectionPointInSketchSpace(1)  ' Get the user's pick point
If (IsEmpty(PickPt) Or IsNull(PickPt)) Then    ' No pick point available
Exit Sub
End If
```

### SafeArray Return Values

The SOLIDWORKS API passes and returns all SafeArrays as a type VARIANT. In many instances, you might find it useful to know the length of a SafeArray returned by SOLIDWORKS. If SOLIDWORKS does not provide a function that counts, such as IFace2::GetEdgeCount, you can use standard MFC or VBA routines to determine the SafeArray length. The following unmanaged C++ and VBA examples show you one way for determining the number of elements in a SafeArray.

```vb
// In unmanaged C++
// Get all of the children components from this m_Component object
VARIANT componentChildren = m_Component.GetChildren();
if ((componentChildren.vt == VT_EMPTY) ||
(V_VT(&componentChildren) == VT_NULL)) // Error - array is empty or null
return;
SafeArray* psa = V_ARRAY(&componentChildren);
LPDISPATCH* componentChildrenArray;
HRESULT hres = SafeArrayAccessData(psa, (void **)&componentChildrenArray);

long highIndex;
SafeArrayGetUBound(psa, 1, &highIndex); // Get index number of highest array element
       // The array range is from 0 to highIndex
long childrenCount = highIndex + 1;  // Actual # of array elements is highIndex + 1
for (int i = 0; i < childrenCount; i++) // For each child component
{
IComponent m_childComponent(componentChildrenArray[i]);
componentChildrenArray[i]->AddRef();

VARIANT_BOOL isSuppressed;   // Perform sample operation using the component
isSuppressed = m_childComponent.IsSuppressed();
}
hres = SafeArrayUnaccessData(psa);  // Release and destroy the
hres = SafeArrayDestroy(psa);   // component SafeArray

' In VBA
' Display the entire version history for the specified file
' Show results in a list box control
Dim fileHistory As Variant
fileHistory = swApp.VersionHistory(filename)
If Not (IsEmpty(fileHistory) Or IsNull(fileHistory)) Then
For i = 0 To UBound(history)   ' For each string in the SafeArray,
myListBox.AddItem (fileHistory(i))  ' Display it in the list box control
Next i
End If
```
