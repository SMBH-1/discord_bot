import React from "react";

function CommandCard({name, description, args, cooldown}) {
  return (
    <div className="card border-dark mb-3" style={{ width: "20rem" }}>
      <div className="card-header">{name}</div>
      <div className="card-body">
        <h5 className="card-title">Description</h5>
        <p className="card-text">
          {description}
        </p>
        {args && 
        <>
        <h5 className="card-title">Arguments</h5>
        <p className="card-text">{args}</p>
        </>
        }
        {cooldown && 
        <>
        <h5 className="card-title">Cooldown</h5>
        <p className="card-text">{cooldown}</p>
        </>
        }
      </div>
    </div>
  );
}

export default CommandCard;
