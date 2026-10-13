---
title: "Get Circular Holes In Face Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Circular_Holes_In_Face_Example_CPlusPlus_COM.htm"
---

# Get Circular Holes In Face Example (C++ COM)

This example shows how to calculate the number of circular holes in a selected face. IEdge::IGetCurveParams2 and ILoop::IGetEdges return arrays, so this code must be used in an in-process DLL. Otherwise, use the methods IEdge::GetCurveParams2 and IEdge::GetEdges that return VARIANTs.

```vb
void GetCountHole1(LPMODELDOC2 pModelDoc, CString* Message)
{
 long lres=0;
 int pCount=0;
 LPSELECTIONMGR pSelectMgr=NULL;
 HRESULT hres=NULL;
 LPUNKNOWN pUnk=NULL;
 LPFACE SelectedFace=NULL;
 LPLOOP pLoop=NULL,pFirstLoop=NULL;
 VARIANT_BOOL pVBool,pCBool;
 LPEDGE pEdge=NULL;
 LPCURVE pCurve=NULL;
 char ch[128];
 short i;
 long pEdgeCount;

 //Form the return message
 *Message = "";

 //Get the selection mgr for this doc
 if(S_OK!=pModelDoc->get_ISelectionManager(&pSelectMgr)||pSelectMgr==NULL)
 {
  *Message+="Unable to get the Selection Manager.\r\n";
 }
else if(S_OK!=pSelectMgr->GetSelectedObjectType(1,&lres)||lres==0)
 {
  //Get the selected object type
  *Message+="No face is currently selected.\r\n";
 }
 else if(S_OK!=pSelectMgr->IGetSelectedObject2(1,&pUnk)||pUnk==NULL)
 {
  //Get the selected object of Unknown Type
  *Message+="Unable to get the selected object.\r\n";
 }
 else if(S_OK!=pUnk->QueryInterface(IID_IFace, (LPVOID *)&SelectedFace)||SelectedFace==NULL)
 {
  //Get the selected face
  *Message+="Unable to get the selected face.\r\n";
 }
 else if(S_OK!=SelectedFace->IGetFirstLoop(&pLoop)||pLoop==NULL)
 {
  //Get the selected loop
  *Message+="Unable to get the selected face first loop.\r\n";
 }
 else
 {
  pFirstLoop=pLoop;
  do
  {
   if(S_OK!=pLoop->IsOuter(&pVBool)||pVBool==TRUE)
   {
//    Check whether the loop is outer
    *Message+="The loop is an outer loop.\r\n";
   }
   else if(S_OK!=pLoop->GetEdgeCount(&pEdgeCount)||pEdgeCount<=0)
   {
//    Check the loop has edges, for example, no vertex loops.
    *Message+="The loop has no edges.\r\n";
   }
   else
   {
//  Allocate the calculated size edge list array and set them to null
    LPEDGE *pEdgeList = new LPEDGE[pEdgeCount];
    for (i=0;i<pEdgeCount;i++)
    {
     pEdgeList[i]=NULL;
    }
//    Get the edge list
    if(S_OK!=pLoop->IGetEdges(&pEdgeList)||*pEdgeList==NULL)
    {
     *Message+="Cannot get the loop edges.\r\n";
    }
    else
    {
//     Allocate the fixed size edge data array
     double* pEdgeData = new double[100];

//     Get the first edge in the list
     pEdge=pEdgeList[0];

     if(S_OK!=pEdge->IGetCurve(&pCurve)||pCurve==NULL)
     {
//      Get the curve
      *Message+="Cannot get the edge curve.\r\n";
     }
    else if(S_OK!=pEdge->IGetCurveParams2(&pEdgeData[0]))
     {
//      Get the data of curve
    *Message+="Failed to get the curve parameters.\r\n";
     }
     else
     {
//      Get the edge curve data
     if(S_OK!=pCurve->IsCircle(&pCBool)||pCBool==FALSE)
      {
//       the curve is not a circle
      *Message+="The curve is not a circle.\r\n";
      }
//      Increment the circular hole count
      else pCount=pCount+1;
     }
//     Release the curve
     if(pCurve!=NULL)pCurve->Release();

     delete pEdgeData;

    }
//    Release the allocated SOLIDWORKS edge list objects
    for (i=0;i<pEdgeCount;i++)
    {
     if(pEdgeList[i]!=NULL)pEdgeList[i]->Release();
    }
    delete pEdgeList;
   }
//  Get the next loop
 }while(S_OK==pLoop->IGetNext(&pLoop)&&pLoop!=NULL&&pLoop!=pFirstLoop);

  int t=sprintf(ch,"%d",pCount);
  CString pStr(ch);
  *Message+="The number of circular holes is " + pStr + ".\r\n";
 }

// Everything is okay.
// ========== == ===== =====
// Release the loop
 if(pLoop!=NULL)pLoop->Release();
// Release the selected face
 if(SelectedFace!=NULL)SelectedFace->Release();
// Release the Selection Manager
 if(pSelectMgr!=NULL)pSelectMgr->Release();
// Release the unknown object
 if(pUnk!=NULL)pUnk->Release();
// Return with report of results including errors
 return;
}
```
